from __future__ import annotations

import argparse
import logging
from pathlib import Path

from .exa_client import ExaSearchClient
from .pipeline import run_ingestion
from .presets import PRESETS
from .types import IngestionSettings

DEFAULT_ALLOWED_DOMAINS = frozenset(
    {
        "mitre.org",
        "owasp.org",
        "nist.gov",
        "cisa.gov",
        "sans.org",
        "github.com",
        "cloud.google.com",
        "learn.microsoft.com",
        "aws.amazon.com",
    }
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ingest cybersecurity corpus via Exa")
    parser.add_argument(
        "--preset",
        choices=sorted(PRESETS.keys()),
        default="default",
        help="Ingestion preset profile.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Optional custom query config JSON. Overrides preset config.",
    )
    parser.add_argument("--db", type=Path, default=Path("data/cyber_corpus.db"))
    parser.add_argument("--jsonl", type=Path, default=Path("data/cyber_docs.jsonl"))
    parser.add_argument("--max-results-per-query", type=int, default=None)
    parser.add_argument("--sleep-between-calls", type=float, default=None)
    parser.add_argument("--min-text-len", type=int, default=None)
    parser.add_argument("--chunk-size", type=int, default=1400)
    parser.add_argument("--chunk-overlap", type=int, default=200)
    parser.add_argument("--budget-usd", type=float, default=None, help="Estimated spend cap for this run.")
    parser.add_argument(
        "--estimated-cost-per-result-usd",
        type=float,
        default=0.002,
        help="Estimated cost per returned result for budget calculations.",
    )
    parser.add_argument(
        "--allow-domain",
        action="append",
        default=[],
        help="Repeat to add allowed domains. If omitted, defaults are used.",
    )
    return parser


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    args = build_parser().parse_args()
    preset = PRESETS[args.preset]
    allowed_domains = frozenset(args.allow_domain) if args.allow_domain else DEFAULT_ALLOWED_DOMAINS

    settings = IngestionSettings(
        config_path=args.config or preset.config_path,
        db_path=args.db,
        jsonl_path=args.jsonl,
        max_results_per_query=args.max_results_per_query or preset.max_results_per_query,
        sleep_between_calls_seconds=args.sleep_between_calls or preset.sleep_between_calls,
        min_text_len=args.min_text_len or preset.min_text_len,
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap,
        allowed_domains=allowed_domains,
        budget_usd=args.budget_usd,
        estimated_cost_per_result_usd=args.estimated_cost_per_result_usd,
    )

    run_ingestion(settings=settings, client=ExaSearchClient())


if __name__ == "__main__":
    main()
