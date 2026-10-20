---
type: entity
title: "ChunkedDocument (ingest/pipeline.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: data-model
path: "src/sec_redteam/ingest/pipeline.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
  - "[[library/knowledge/private/codebase-graph/concepts/insert-before-export]]"
sources:
  - "src/sec_redteam/ingest/pipeline.py:22-32"
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
  - "chunks"
---

# ChunkedDocument (ingest/pipeline.py)

## Overview

Frozen, slotted dataclass carrying document metadata and a list of text chunks; it does not contain the full text or content hash fields used in DocumentRecord. `src/sec_redteam/ingest/pipeline.py:21`

## Signature / Definition

```python
class ChunkedDocument:
    id: str
    topic: str
    query: str
    title: str
    url: str
    domain: str
    published_at: str | None
    fetched_at: str
    text_len: int
    chunks: list[str]
```

`src/sec_redteam/ingest/pipeline.py:22-32`.

## Behavior

- Frozen, slotted dataclass carrying document metadata and a list of text chunks; it does not contain the full text or content hash fields used in DocumentRecord. `src/sec_redteam/ingest/pipeline.py:21`
- Created after insert_doc succeeds and serialized as one JSONL record. `src/sec_redteam/ingest/pipeline.py:144`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] (calls) — `src/sec_redteam/ingest/pipeline.py:144`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]] — `src/sec_redteam/ingest/pipeline.py:22-32`.
- [[library/knowledge/private/codebase-graph/concepts/insert-before-export]] — `src/sec_redteam/ingest/pipeline.py:22-32`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/pipeline.py:22-32`.
