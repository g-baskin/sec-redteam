---
type: entity
title: "_load_queries (ingest/pipeline.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: function
path: "src/sec_redteam/ingest/pipeline.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
sources:
  - "src/sec_redteam/ingest/pipeline.py:54-61"
---

# _load_queries (ingest/pipeline.py)

## Overview

Reads JSON from the supplied path and coerces each topic and query to strings; it does not perform a separate schema-validation pass. `src/sec_redteam/ingest/pipeline.py:54`

## Signature / Definition

```python
def _load_queries(config_path: Path) -> dict[str, list[str]]:
```

`src/sec_redteam/ingest/pipeline.py:54-61`.

## Behavior

- Reads JSON from the supplied path and coerces each topic and query to strings; it does not perform a separate schema-validation pass. `src/sec_redteam/ingest/pipeline.py:54`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] (calls) — `src/sec_redteam/ingest/pipeline.py:72`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]] — `src/sec_redteam/ingest/pipeline.py:54-61`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/pipeline.py:54-61`.
