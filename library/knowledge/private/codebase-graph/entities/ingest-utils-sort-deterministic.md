---
type: entity
title: "sort_deterministic (ingest/utils.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: function
path: "src/sec_redteam/ingest/utils.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-module]]"
sources:
  - "src/sec_redteam/ingest/utils.py:44-45"
---

# sort_deterministic (ingest/utils.py)

## Overview

Returns sorted(values) as a new list; it does not deduplicate values. `src/sec_redteam/ingest/utils.py:45`

## Signature / Definition

```python
def sort_deterministic(values: Iterable[str]) -> list[str]:
```

`src/sec_redteam/ingest/utils.py:44-45`.

## Behavior

- Returns sorted(values) as a new list; it does not deduplicate values. `src/sec_redteam/ingest/utils.py:45`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] (calls) — `src/sec_redteam/ingest/pipeline.py:81`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-utils-module]] — `src/sec_redteam/ingest/utils.py:44-45`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/utils.py:44-45`.
