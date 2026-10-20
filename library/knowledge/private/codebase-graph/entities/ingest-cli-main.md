---
type: entity
title: "main (ingest/cli.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: function
path: "src/sec_redteam/ingest/cli.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-build-parser]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-ExaSearchClient]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-types-IngestionSettings]]"
used_by: []
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-module]]"
  - "[[library/knowledge/private/codebase-graph/concepts/corpus-filter-and-budget]]"
sources:
  - "src/sec_redteam/ingest/cli.py:64-88"
---

# main (ingest/cli.py)

## Overview

Parses arguments and selects the preset. `src/sec_redteam/ingest/cli.py:70`

## Signature / Definition

```python
def main() -> None:
```

`src/sec_redteam/ingest/cli.py:64-88`.

## Behavior

- Parses arguments and selects the preset. `src/sec_redteam/ingest/cli.py:70`
- Any supplied allow-domain values replace the defaults. `src/sec_redteam/ingest/cli.py:72`
- Numeric preset overrides use truthiness; zero falls back to the preset. `src/sec_redteam/ingest/cli.py:78`
- Constructs ExaSearchClient and invokes ingestion; this entry point performs live external searches when run. `src/sec_redteam/ingest/cli.py:88`

## Connections

- calls [[library/knowledge/private/codebase-graph/entities/ingest-cli-build-parser]] — `src/sec_redteam/ingest/cli.py:70`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-ExaSearchClient]] — `src/sec_redteam/ingest/cli.py:88`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] — `src/sec_redteam/ingest/cli.py:88`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-types-IngestionSettings]] — `src/sec_redteam/ingest/cli.py:74`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-cli-module]] — `src/sec_redteam/ingest/cli.py:64-88`.
- [[library/knowledge/private/codebase-graph/concepts/corpus-filter-and-budget]] — `src/sec_redteam/ingest/cli.py:64-88`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/cli.py:64-88`.
