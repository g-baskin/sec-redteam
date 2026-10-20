---
type: entity
title: "IngestionSettings (ingest/types.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: data-model
path: "src/sec_redteam/ingest/types.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-main]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-types-module]]"
sources:
  - "src/sec_redteam/ingest/types.py:8-19"
schema_library: dataclasses
fields:
  - "config_path"
  - "db_path"
  - "jsonl_path"
  - "max_results_per_query"
  - "sleep_between_calls_seconds"
  - "min_text_len"
  - "chunk_size"
  - "chunk_overlap"
  - "allowed_domains"
  - "budget_usd"
  - "estimated_cost_per_result_usd"
---

# IngestionSettings (ingest/types.py)

## Overview

Frozen, slotted dataclass defining input/output paths, search limits, chunk sizes, domain allowlist and estimated budget settings. `src/sec_redteam/ingest/types.py:7`

## Signature / Definition

```python
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
```

`src/sec_redteam/ingest/types.py:8-19`.

## Behavior

- Frozen, slotted dataclass defining input/output paths, search limits, chunk sizes, domain allowlist and estimated budget settings. `src/sec_redteam/ingest/types.py:7`
- The declaration contains annotated fields only, with no __post_init__ validation method. `src/sec_redteam/ingest/types.py:8`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-cli-main]] (calls) — `src/sec_redteam/ingest/cli.py:74`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-types-module]] — `src/sec_redteam/ingest/types.py:8-19`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/types.py:8-19`.
