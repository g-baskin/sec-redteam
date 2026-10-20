---
type: entity
title: "IngestPreset (ingest/presets.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: data-model
path: "src/sec_redteam/ingest/presets.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by: []
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-presets-module]]"
sources:
  - "src/sec_redteam/ingest/presets.py:8-12"
schema_library: dataclasses
fields:
  - "config_path"
  - "max_results_per_query"
  - "min_text_len"
  - "sleep_between_calls"
---

# IngestPreset (ingest/presets.py)

## Overview

Frozen, slotted dataclass containing config_path, max_results_per_query, min_text_len and sleep_between_calls. `src/sec_redteam/ingest/presets.py:7`

## Signature / Definition

```python
class IngestPreset:
    config_path: Path
    max_results_per_query: int
    min_text_len: int
    sleep_between_calls: float
```

`src/sec_redteam/ingest/presets.py:8-12`.

## Behavior

- Frozen, slotted dataclass containing config_path, max_results_per_query, min_text_len and sleep_between_calls. `src/sec_redteam/ingest/presets.py:7`

## Connections

- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-presets-module]] — `src/sec_redteam/ingest/presets.py:8-12`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/presets.py:8-12`.
