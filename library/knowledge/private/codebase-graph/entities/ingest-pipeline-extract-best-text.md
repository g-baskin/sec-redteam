---
type: entity
title: "_extract_best_text (ingest/pipeline.py)"
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
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-looks-like-html]]"
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
sources:
  - "src/sec_redteam/ingest/pipeline.py:44-51"
---

# _extract_best_text (ingest/pipeline.py)

## Overview

Returns an empty string for empty input and preserves input not recognized as HTML. `src/sec_redteam/ingest/pipeline.py:45`

## Signature / Definition

```python
def _extract_best_text(raw_text: str) -> str:
```

`src/sec_redteam/ingest/pipeline.py:44-51`.

## Behavior

- Returns an empty string for empty input and preserves input not recognized as HTML. `src/sec_redteam/ingest/pipeline.py:45`
- Calls trafilatura.extract without comments or tables; falls back to the original text if extraction is empty. `src/sec_redteam/ingest/pipeline.py:50`

## Connections

- calls [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-looks-like-html]] — `src/sec_redteam/ingest/pipeline.py:47`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] (calls) — `src/sec_redteam/ingest/pipeline.py:120`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]] — `src/sec_redteam/ingest/pipeline.py:44-51`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/pipeline.py:44-51`.
