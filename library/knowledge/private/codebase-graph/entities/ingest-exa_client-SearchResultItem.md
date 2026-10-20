---
type: entity
title: "SearchResultItem (ingest/exa_client.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: data-model
path: "src/sec_redteam/ingest/exa_client.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-ExaSearchClient]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]]"
sources:
  - "src/sec_redteam/ingest/exa_client.py:12-16"
schema_library: dataclasses
fields:
  - "title"
  - "url"
  - "text"
  - "published_date"
---

# SearchResultItem (ingest/exa_client.py)

## Overview

Frozen, slotted dataclass with title, url, text and optional published_date fields. `src/sec_redteam/ingest/exa_client.py:11`

## Signature / Definition

```python
class SearchResultItem:
    title: str
    url: str
    text: str
    published_date: str | None
```

`src/sec_redteam/ingest/exa_client.py:12-16`.

## Behavior

- Frozen, slotted dataclass with title, url, text and optional published_date fields. `src/sec_redteam/ingest/exa_client.py:11`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-ExaSearchClient]] (calls) — `src/sec_redteam/ingest/exa_client.py:38`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]] — `src/sec_redteam/ingest/exa_client.py:12-16`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/exa_client.py:12-16`.
