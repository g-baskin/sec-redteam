---
type: entity
title: "SearchClient (ingest/exa_client.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: class
path: "src/sec_redteam/ingest/exa_client.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by: []
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]]"
sources:
  - "src/sec_redteam/ingest/exa_client.py:19-21"
---

# SearchClient (ingest/exa_client.py)

## Overview

Protocol declaring search_and_contents(query, num_results) returning a list of SearchResultItem; the method body is an ellipsis. `src/sec_redteam/ingest/exa_client.py:19`

## Signature / Definition

```python
class SearchClient(Protocol):
    def search_and_contents(self, query: str, num_results: int) -> list[SearchResultItem]:
```

`src/sec_redteam/ingest/exa_client.py:19-21`.

## Behavior

- Protocol declaring search_and_contents(query, num_results) returning a list of SearchResultItem; the method body is an ellipsis. `src/sec_redteam/ingest/exa_client.py:19`

## Connections

- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]] — `src/sec_redteam/ingest/exa_client.py:19-21`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/exa_client.py:19-21`.
