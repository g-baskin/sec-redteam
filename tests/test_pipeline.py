from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from sec_redteam.ingest.pipeline import run_ingestion
from sec_redteam.ingest.types import IngestionSettings


@dataclass(slots=True, frozen=True)
class FakeResult:
    title: str
    url: str
    text: str
    published_date: str | None


class FakeClient:
    def search_and_contents(self, query: str, num_results: int) -> list[FakeResult]:
        _ = (query, num_results)
        return [
            FakeResult(
                title="Doc",
                url="https://owasp.org/example",
                text="A" * 2000,
                published_date=None,
            )
        ]


class MultiQueryClient:
    def search_and_contents(self, query: str, num_results: int) -> list[FakeResult]:
        _ = num_results
        return [
            FakeResult(
                title=f"Doc {query}",
                url=f"https://owasp.org/{query}",
                text="A" * 2000,
                published_date=None,
            )
        ]


def test_run_ingestion_writes_outputs(tmp_path: Path) -> None:
    config_path = tmp_path / "queries.json"
    config_path.write_text(json.dumps({"topic": ["query"]}), encoding="utf-8")

    db_path = tmp_path / "out.db"
    jsonl_path = tmp_path / "out.jsonl"

    settings = IngestionSettings(
        config_path=config_path,
        db_path=db_path,
        jsonl_path=jsonl_path,
        max_results_per_query=5,
        sleep_between_calls_seconds=0,
        min_text_len=100,
        chunk_size=300,
        chunk_overlap=50,
        allowed_domains=frozenset({"owasp.org"}),
        budget_usd=None,
        estimated_cost_per_result_usd=0.002,
    )

    saved = run_ingestion(settings, client=FakeClient())
    assert saved == 1
    assert db_path.exists()
    assert jsonl_path.exists()

    lines = jsonl_path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 1


def test_budget_cap_stops_early(tmp_path: Path) -> None:
    config_path = tmp_path / "queries.json"
    config_path.write_text(json.dumps({"topic": ["q1", "q2", "q3"]}), encoding="utf-8")

    settings = IngestionSettings(
        config_path=config_path,
        db_path=tmp_path / "out.db",
        jsonl_path=tmp_path / "out.jsonl",
        max_results_per_query=10,
        sleep_between_calls_seconds=0,
        min_text_len=100,
        chunk_size=300,
        chunk_overlap=50,
        allowed_domains=frozenset({"owasp.org"}),
        budget_usd=0.003,
        estimated_cost_per_result_usd=0.002,
    )

    saved = run_ingestion(settings, client=MultiQueryClient())
    assert saved == 1
