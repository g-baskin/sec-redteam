---
type: entity
title: "build_parser (ingest/cli.py)"
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
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-main]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-module]]"
sources:
  - "src/sec_redteam/ingest/cli.py:27-61"
---

# build_parser (ingest/cli.py)

## Overview

Builds the ingestion argument parser; numeric override options default to None. `src/sec_redteam/ingest/cli.py:27`

## Signature / Definition

```python
def build_parser() -> argparse.ArgumentParser:
```

`src/sec_redteam/ingest/cli.py:27-61`.

## Behavior

- Builds the ingestion argument parser; numeric override options default to None. `src/sec_redteam/ingest/cli.py:27`
- Defaults chunk size to 1400 characters and overlap to 200. `src/sec_redteam/ingest/cli.py:46`
- Accepts repeatable --allow-domain values; its help text says add, while main chooses replacement semantics. `src/sec_redteam/ingest/cli.py:55`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-cli-main]] (calls) — `src/sec_redteam/ingest/cli.py:70`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-cli-module]] — `src/sec_redteam/ingest/cli.py:27-61`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/cli.py:27-61`.
