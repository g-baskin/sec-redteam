---
type: entity
title: "chunk_text (ingest/utils.py)"
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
  - "[[library/knowledge/private/codebase-graph/concepts/insert-before-export]]"
sources:
  - "src/sec_redteam/ingest/utils.py:25-41"
---

# chunk_text (ingest/utils.py)

## Overview

Rejects nonpositive chunk sizes, negative overlaps and overlaps greater than or equal to chunk size with ValueError. `src/sec_redteam/ingest/utils.py:26`

## Signature / Definition

```python
def chunk_text(text: str, *, chunk_size: int, chunk_overlap: int) -> list[str]:
```

`src/sec_redteam/ingest/utils.py:25-41`.

## Behavior

- Rejects nonpositive chunk sizes, negative overlaps and overlaps greater than or equal to chunk size with ValueError. `src/sec_redteam/ingest/utils.py:26`
- Slices Python strings with stride chunk_size minus chunk_overlap; units are characters, not model tokens. `src/sec_redteam/ingest/utils.py:34`
- An empty input yields an empty list; a trailing partial slice is retained. `src/sec_redteam/ingest/utils.py:37`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] (calls) — `src/sec_redteam/ingest/pipeline.py:154`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-utils-module]] — `src/sec_redteam/ingest/utils.py:25-41`.
- [[library/knowledge/private/codebase-graph/concepts/insert-before-export]] — `src/sec_redteam/ingest/utils.py:25-41`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/utils.py:25-41`.
