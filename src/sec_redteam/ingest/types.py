from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True, frozen=True)
class IngestionSettings:
    config_path: Path
    db_path: Path
    jsonl_path: Path
    max_results_per_query: int
    sleep_between_calls_seconds: float
    min_text_len: int
    chunk_size: int
    chunk_overlap: int
    allowed_domains: frozenset[str]
    budget_usd: float | None
    estimated_cost_per_result_usd: float
