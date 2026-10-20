---
type: entity
title: "insert_doc (ingest/storage.py)"
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
  - "[[library/knowledge/private/codebase-graph/concepts/insert-before-export]]"
sources:
  - "src/sec_redteam/ingest/storage.py:49-75"
---

# insert_doc (ingest/storage.py)

## Overview

Uses bound parameters to insert all DocumentRecord fields. `src/sec_redteam/ingest/storage.py:51`

## Signature / Definition

```python
def insert_doc(conn: sqlite3.Connection, record: DocumentRecord) -> bool:
```

`src/sec_redteam/ingest/storage.py:49-75`.

## Behavior

- Uses bound parameters to insert all DocumentRecord fields. `src/sec_redteam/ingest/storage.py:51`
- Commits and returns True after insertion; catches sqlite3.IntegrityError and returns False instead of refreshing an existing row. `src/sec_redteam/ingest/storage.py:72`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] (calls) — `src/sec_redteam/ingest/pipeline.py:141`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-storage-module]] — `src/sec_redteam/ingest/storage.py:49-75`.
- [[library/knowledge/private/codebase-graph/concepts/insert-before-export]] — `src/sec_redteam/ingest/storage.py:49-75`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/storage.py:49-75`.
