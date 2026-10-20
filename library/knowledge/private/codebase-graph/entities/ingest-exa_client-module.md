---
type: entity
title: "ingest/exa_client.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/ingest/exa_client.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-ExaSearchClient]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchClient]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchResultItem]]"
sources:
  - "src/sec_redteam/ingest/exa_client.py:1"
exports:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-ExaSearchClient]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchClient]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchResultItem]]"
imports: []
---

# ingest/exa_client.py

## Overview

Search-result model, search protocol and Exa SDK adapter declarations. `src/sec_redteam/ingest/exa_client.py:1`

## Signature / Definition

Source module: `src/sec_redteam/ingest/exa_client.py:1`.

Declarations (one entity per linked page):
- [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-ExaSearchClient]] — `src/sec_redteam/ingest/exa_client.py:24-46`.
- [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchClient]] — `src/sec_redteam/ingest/exa_client.py:19-21`.
- [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchResultItem]] — `src/sec_redteam/ingest/exa_client.py:12-16`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/ingest/exa_client.py:1`.

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-cli-module]] (imports) — `src/sec_redteam/ingest/cli.py:7`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]] (imports) — `src/sec_redteam/ingest/pipeline.py:13`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-ExaSearchClient]] — `src/sec_redteam/ingest/exa_client.py:24-46`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchClient]] — `src/sec_redteam/ingest/exa_client.py:19-21`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchResultItem]] — `src/sec_redteam/ingest/exa_client.py:12-16`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/exa_client.py:1`.
