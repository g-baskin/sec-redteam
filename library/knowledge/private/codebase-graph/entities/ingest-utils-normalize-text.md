---
type: entity
title: "normalize_text (ingest/utils.py)"
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
  - "src/sec_redteam/ingest/utils.py:16-18"
---

# normalize_text (ingest/utils.py)

## Overview

Replaces null characters with spaces, collapses runs of whitespace and strips surrounding whitespace. `src/sec_redteam/ingest/utils.py:17`

## Signature / Definition

```python
def normalize_text(text: str) -> str:
```

`src/sec_redteam/ingest/utils.py:16-18`.

## Behavior

- Replaces null characters with spaces, collapses runs of whitespace and strips surrounding whitespace. `src/sec_redteam/ingest/utils.py:17`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] (calls) — `src/sec_redteam/ingest/pipeline.py:120`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-utils-module]] — `src/sec_redteam/ingest/utils.py:16-18`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/utils.py:16-18`.
