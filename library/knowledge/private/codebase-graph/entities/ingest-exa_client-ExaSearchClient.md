---
type: entity
title: "ExaSearchClient (ingest/exa_client.py)"
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
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchResultItem]]"
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-main]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]]"
sources:
  - "src/sec_redteam/ingest/exa_client.py:24-46"
---

# ExaSearchClient (ingest/exa_client.py)

## Overview

Construction calls load_dotenv, takes an explicit key or EXA_API_KEY, and raises ValueError if absent. `src/sec_redteam/ingest/exa_client.py:25`

## Signature / Definition

```python
class ExaSearchClient:
    def __init__(self, api_key: str | None = None) -> None:
    def search_and_contents(self, query: str, num_results: int) -> list[SearchResultItem]:
```

`src/sec_redteam/ingest/exa_client.py:24-46`.

## Behavior

- Construction calls load_dotenv, takes an explicit key or EXA_API_KEY, and raises ValueError if absent. `src/sec_redteam/ingest/exa_client.py:25`
- Constructs the external Exa SDK client. `src/sec_redteam/ingest/exa_client.py:30`
- search_and_contents requests text=True and converts each result into SearchResultItem; missing textual values become empty strings. `src/sec_redteam/ingest/exa_client.py:32`

## Connections

- calls [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchResultItem]] — `src/sec_redteam/ingest/exa_client.py:38`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-cli-main]] (calls) — `src/sec_redteam/ingest/cli.py:88`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]] — `src/sec_redteam/ingest/exa_client.py:24-46`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/exa_client.py:24-46`.
