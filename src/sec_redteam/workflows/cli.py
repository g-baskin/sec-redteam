from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from .evidence import fetch_evidence_sources
from .models import WorkflowType
from .planner import build_workflow_plan


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate red/blue/purple workflow plans")
    parser.add_argument("--type", choices=["red", "blue", "purple"], default="red")
    parser.add_argument("--scenario", required=True, help="Scenario name, e.g. phishing to credential abuse")
    parser.add_argument("--scope", default="lab", help="Plan output label only; not an execution boundary.")
    parser.add_argument("--db", type=Path, default=Path("data/cyber_corpus.db"), help="Corpus SQLite DB")
    parser.add_argument("--evidence-limit", type=int, default=10, help="Max supporting sources")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    workflow_type = args.type
    evidence = fetch_evidence_sources(
        db_path=args.db,
        scenario=args.scenario,
        workflow_type=workflow_type,
        limit=args.evidence_limit,
    )
    plan = build_workflow_plan(
        workflow_type=workflow_type,  # type: ignore[arg-type]
        scenario=args.scenario,
        scope=args.scope,
        evidence_sources=evidence,
    )
    print(json.dumps(asdict(plan), indent=2))


if __name__ == "__main__":
    main()
