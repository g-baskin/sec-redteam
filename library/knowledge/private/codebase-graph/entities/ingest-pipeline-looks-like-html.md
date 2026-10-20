---
type: entity
title: "_looks_like_html (ingest/pipeline.py)"
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
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-extract-best-text]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
sources:
  - "src/sec_redteam/ingest/pipeline.py:38-41"
---

# _looks_like_html (ingest/pipeline.py)

## Overview

Requires both angle brackets, then searches the HTML marker regex declared at line 35; this is a heuristic, not HTML validation. `src/sec_redteam/ingest/pipeline.py:38`

## Signature / Definition

```python
def _looks_like_html(text: str) -> bool:
```

`src/sec_redteam/ingest/pipeline.py:38-41`.

## Behavior

- Requires both angle brackets, then searches the HTML marker regex declared at line 35; this is a heuristic, not HTML validation. `src/sec_redteam/ingest/pipeline.py:38`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-extract-best-text]] (calls) — `src/sec_redteam/ingest/pipeline.py:47`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]] — `src/sec_redteam/ingest/pipeline.py:38-41`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/pipeline.py:38-41`.
