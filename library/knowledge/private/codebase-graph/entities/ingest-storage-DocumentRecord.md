---
type: entity
title: "DocumentRecord (ingest/storage.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: data-model
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
  - "src/sec_redteam/ingest/storage.py:9-20"
schema_library: dataclasses
fields:
  - "id"
  - "topic"
  - "query"
  - "title"
  - "url"
  - "domain"
  - "published_at"
  - "fetched_at"
  - "text_len"
  - "text"
  - "sha256"
---

# DocumentRecord (ingest/storage.py)

## Overview

Frozen, slotted dataclass carrying metadata, full cleaned text and a SHA-256 content hash. `src/sec_redteam/ingest/storage.py:8`

## Signature / Definition

```python
class DocumentRecord:
    id: str
    topic: str
    query: str
    title: str
    url: str
    domain: str
    published_at: str | None
    fetched_at: str
    text_len: int
    text: str
    sha256: str
```

`src/sec_redteam/ingest/storage.py:9-20`.

## Behavior

- Frozen, slotted dataclass carrying metadata, full cleaned text and a SHA-256 content hash. `src/sec_redteam/ingest/storage.py:8`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] (calls) — `src/sec_redteam/ingest/pipeline.py:127`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-storage-module]] — `src/sec_redteam/ingest/storage.py:9-20`.
- [[library/knowledge/private/codebase-graph/concepts/insert-before-export]] — `src/sec_redteam/ingest/storage.py:9-20`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/storage.py:9-20`.
