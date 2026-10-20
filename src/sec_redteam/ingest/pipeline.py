from __future__ import annotations

import json
import logging
import re
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

import trafilatura

from .exa_client import SearchClient
from .storage import DocumentRecord, init_db, insert_doc
from .types import IngestionSettings
from .utils import chunk_text, domain_of, normalize_text, sha256_text, sort_deterministic

logger = logging.getLogger(__name__)


@dataclass(slots=True, frozen=True)
class ChunkedDocument:
    id: str
    topic: str
    query: str
    title: str
    url: str
    domain: str
    published_at: str | None
    fetched_at: str
    text_len: int
    chunks: list[str]


HTML_MARKER_PATTERN = re.compile(r"<\s*(?:html|body|article|div|p|h1|h2|h3|section|main)\b", re.IGNORECASE)


def _looks_like_html(text: str) -> bool:
    if "<" not in text or ">" not in text:
        return False
    return bool(HTML_MARKER_PATTERN.search(text))


def _extract_best_text(raw_text: str) -> str:
    if not raw_text:
        return ""
    if not _looks_like_html(raw_text):
        return raw_text

    extracted = trafilatura.extract(raw_text, include_comments=False, include_tables=False)
    return extracted if extracted else raw_text


def _load_queries(config_path: Path) -> dict[str, list[str]]:
    with config_path.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    parsed: dict[str, list[str]] = {}
    for topic, queries in payload.items():
        parsed[str(topic)] = [str(query) for query in queries]
    return parsed


def _domain_allowed(url: str, allowed_domains: frozenset[str]) -> bool:
    if not allowed_domains:
        return True
    return domain_of(url) in allowed_domains


def run_ingestion(settings: IngestionSettings, client: SearchClient) -> int:
    started = time.perf_counter()
    queries = _load_queries(settings.config_path)
    conn = init_db(settings.db_path)
    settings.jsonl_path.parent.mkdir(parents=True, exist_ok=True)

    saved_count = 0
    seen_urls: set[str] = set()
    estimated_spend_usd = 0.0

    with settings.jsonl_path.open("a", encoding="utf-8") as output:
        for topic in sort_deterministic(queries.keys()):
            topic_queries = sort_deterministic(queries[topic])
            for query in topic_queries:
                call_started = time.perf_counter()
                try:
                    results = client.search_and_contents(query, settings.max_results_per_query)
                    logger.info(
                        "exa_search_ok",
                        extra={
                            "query": query,
                            "topic": topic,
                            "result_count": len(results),
                            "elapsed_seconds": round(time.perf_counter() - call_started, 4),
                        },
                    )
                except Exception:
                    logger.exception("exa_search_failed", extra={"query": query, "topic": topic})
                    continue

                estimated_spend_usd += len(results) * settings.estimated_cost_per_result_usd
                if settings.budget_usd is not None and estimated_spend_usd >= settings.budget_usd:
                    logger.info(
                        "budget_cap_reached",
                        extra={
                            "estimated_spend_usd": round(estimated_spend_usd, 4),
                            "budget_usd": settings.budget_usd,
                            "topic": topic,
                            "query": query,
                        },
                    )
                    break

                for result in results:
                    if not result.url or result.url in seen_urls:
                        continue
                    if not _domain_allowed(result.url, settings.allowed_domains):
                        continue
                    seen_urls.add(result.url)

                    cleaned = normalize_text(_extract_best_text(result.text))
                    if len(cleaned) < settings.min_text_len:
                        continue

                    fetched_at = datetime.now(timezone.utc).isoformat()
                    digest = sha256_text(cleaned)
                    doc_id = sha256_text(result.url)[:24]
                    record = DocumentRecord(
                        id=doc_id,
                        topic=topic,
                        query=query,
                        title=result.title,
                        url=result.url,
                        domain=domain_of(result.url),
                        published_at=result.published_date,
                        fetched_at=fetched_at,
                        text_len=len(cleaned),
                        text=cleaned,
                        sha256=digest,
                    )

                    if not insert_doc(conn, record):
                        continue

                    chunked = ChunkedDocument(
                        id=doc_id,
                        topic=topic,
                        query=query,
                        title=result.title,
                        url=result.url,
                        domain=domain_of(result.url),
                        published_at=result.published_date,
                        fetched_at=fetched_at,
                        text_len=len(cleaned),
                        chunks=chunk_text(
                            cleaned,
                            chunk_size=settings.chunk_size,
                            chunk_overlap=settings.chunk_overlap,
                        ),
                    )
                    output.write(json.dumps(asdict(chunked), ensure_ascii=False) + "\n")
                    saved_count += 1

                if settings.budget_usd is not None and estimated_spend_usd >= settings.budget_usd:
                    break

                time.sleep(settings.sleep_between_calls_seconds)

            if settings.budget_usd is not None and estimated_spend_usd >= settings.budget_usd:
                break

    logger.info(
        "ingestion_complete",
        extra={
            "saved_count": saved_count,
            "estimated_spend_usd": round(estimated_spend_usd, 4),
            "elapsed_seconds": round(time.perf_counter() - started, 4),
            "db_path": str(settings.db_path),
            "jsonl_path": str(settings.jsonl_path),
        },
    )
    return saved_count
