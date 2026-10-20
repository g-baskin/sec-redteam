from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True, frozen=True)
class IngestPreset:
    config_path: Path
    max_results_per_query: int
    min_text_len: int
    sleep_between_calls: float


PRESETS: dict[str, IngestPreset] = {
    "default": IngestPreset(
        config_path=Path("src/sec_redteam/ingest/default_queries.json"),
        max_results_per_query=50,
        min_text_len=1200,
        sleep_between_calls=0.7,
    ),
    "badass-today": IngestPreset(
        config_path=Path("src/sec_redteam/ingest/badass_today_queries.json"),
        max_results_per_query=20,
        min_text_len=900,
        sleep_between_calls=0.4,
    ),
    "offsec-research": IngestPreset(
        config_path=Path("src/sec_redteam/ingest/offsec_research_queries.json"),
        max_results_per_query=20,
        min_text_len=1000,
        sleep_between_calls=0.5,
    ),
    "max-coverage": IngestPreset(
        config_path=Path("src/sec_redteam/ingest/offsec_research_queries.json"),
        max_results_per_query=50,
        min_text_len=500,
        sleep_between_calls=0.2,
    ),
    "aggressive-breadth": IngestPreset(
        config_path=Path("src/sec_redteam/ingest/aggressive_breadth_queries.json"),
        max_results_per_query=60,
        min_text_len=400,
        sleep_between_calls=0.15,
    ),
    "compliance-surge": IngestPreset(
        config_path=Path("src/sec_redteam/ingest/compliance_surge_queries.json"),
        max_results_per_query=80,
        min_text_len=300,
        sleep_between_calls=0.1,
    ),
    "compliance-deep": IngestPreset(
        config_path=Path("src/sec_redteam/ingest/compliance_deep_queries.json"),
        max_results_per_query=100,
        min_text_len=200,
        sleep_between_calls=0.05,
    ),
    "playbook-surge": IngestPreset(
        config_path=Path("src/sec_redteam/ingest/playbook_surge_queries.json"),
        max_results_per_query=80,
        min_text_len=150,
        sleep_between_calls=0.1,
    ),
}
