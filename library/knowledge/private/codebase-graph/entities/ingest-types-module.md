---
type: entity
title: "ingest/types.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/ingest/types.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-types-IngestionSettings]]"
sources:
  - "src/sec_redteam/ingest/types.py:1"
exports:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-types-IngestionSettings]]"
imports: []
---

# ingest/types.py

## Overview

Ingestion settings dataclass declaration. `src/sec_redteam/ingest/types.py:1`

## Signature / Definition

Source module: `src/sec_redteam/ingest/types.py:1`.

Declarations (one entity per linked page):
- [[library/knowledge/private/codebase-graph/entities/ingest-types-IngestionSettings]] — `src/sec_redteam/ingest/types.py:8-19`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/ingest/types.py:1`.

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-cli-module]] (imports) — `src/sec_redteam/ingest/cli.py:10`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]] (imports) — `src/sec_redteam/ingest/pipeline.py:15`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-types-IngestionSettings]] — `src/sec_redteam/ingest/types.py:8-19`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/types.py:1`.
