---
type: entity
title: "ingest/storage.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/ingest/storage.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-DocumentRecord]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-init-db]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-insert-doc]]"
sources:
  - "src/sec_redteam/ingest/storage.py:1"
exports:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-DocumentRecord]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-init-db]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-insert-doc]]"
imports: []
---

# ingest/storage.py

## Overview

Document record model and SQLite creation/insertion functions. `src/sec_redteam/ingest/storage.py:1`

## Signature / Definition

Source module: `src/sec_redteam/ingest/storage.py:1`.

Declarations (one entity per linked page):
- [[library/knowledge/private/codebase-graph/entities/ingest-storage-DocumentRecord]] — `src/sec_redteam/ingest/storage.py:9-20`.
- [[library/knowledge/private/codebase-graph/entities/ingest-storage-init-db]] — `src/sec_redteam/ingest/storage.py:23-46`.
- [[library/knowledge/private/codebase-graph/entities/ingest-storage-insert-doc]] — `src/sec_redteam/ingest/storage.py:49-75`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/ingest/storage.py:1`.

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]] (imports) — `src/sec_redteam/ingest/pipeline.py:14`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-storage-DocumentRecord]] — `src/sec_redteam/ingest/storage.py:9-20`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-storage-init-db]] — `src/sec_redteam/ingest/storage.py:23-46`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-storage-insert-doc]] — `src/sec_redteam/ingest/storage.py:49-75`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/storage.py:1`.
