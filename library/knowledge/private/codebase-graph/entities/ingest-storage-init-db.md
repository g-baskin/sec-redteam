---
type: entity
title: "init_db (ingest/storage.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: function
path: "src/sec_redteam/ingest/storage.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-module]]"
sources:
  - "src/sec_redteam/ingest/storage.py:23-46"
---

# init_db (ingest/storage.py)

## Overview

Creates parent directories, opens SQLite and creates docs if absent. `src/sec_redteam/ingest/storage.py:24`

## Signature / Definition

```python
def init_db(path: Path) -> sqlite3.Connection:
```

`src/sec_redteam/ingest/storage.py:23-46`.

## Behavior

- Creates parent directories, opens SQLite and creates docs if absent. `src/sec_redteam/ingest/storage.py:24`
- The docs schema has id as primary key and sha256 as a unique column. `src/sec_redteam/ingest/storage.py:28`
- Creates domain/topic indexes, commits schema work and returns the open connection to the caller. `src/sec_redteam/ingest/storage.py:43`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] (calls) — `src/sec_redteam/ingest/pipeline.py:73`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-storage-module]] — `src/sec_redteam/ingest/storage.py:23-46`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/storage.py:23-46`.
