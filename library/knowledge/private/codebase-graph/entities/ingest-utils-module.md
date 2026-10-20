---
type: entity
title: "ingest/utils.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/ingest/utils.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-chunk-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-domain-of]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-normalize-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-sha256-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-sort-deterministic]]"
sources:
  - "src/sec_redteam/ingest/utils.py:1"
exports:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-chunk-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-domain-of]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-normalize-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-sha256-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-sort-deterministic]]"
imports: []
---

# ingest/utils.py

## Overview

Domain, normalization, hashing, character-chunking and sorting helpers. `src/sec_redteam/ingest/utils.py:1`

## Signature / Definition

Source module: `src/sec_redteam/ingest/utils.py:1`.

Declarations (one entity per linked page):
- [[library/knowledge/private/codebase-graph/entities/ingest-utils-chunk-text]] — `src/sec_redteam/ingest/utils.py:25-41`.
- [[library/knowledge/private/codebase-graph/entities/ingest-utils-domain-of]] — `src/sec_redteam/ingest/utils.py:10-13`.
- [[library/knowledge/private/codebase-graph/entities/ingest-utils-normalize-text]] — `src/sec_redteam/ingest/utils.py:16-18`.
- [[library/knowledge/private/codebase-graph/entities/ingest-utils-sha256-text]] — `src/sec_redteam/ingest/utils.py:21-22`.
- [[library/knowledge/private/codebase-graph/entities/ingest-utils-sort-deterministic]] — `src/sec_redteam/ingest/utils.py:44-45`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/ingest/utils.py:1`.

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]] (imports) — `src/sec_redteam/ingest/pipeline.py:16`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-utils-chunk-text]] — `src/sec_redteam/ingest/utils.py:25-41`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-utils-domain-of]] — `src/sec_redteam/ingest/utils.py:10-13`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-utils-normalize-text]] — `src/sec_redteam/ingest/utils.py:16-18`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-utils-sha256-text]] — `src/sec_redteam/ingest/utils.py:21-22`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-utils-sort-deterministic]] — `src/sec_redteam/ingest/utils.py:44-45`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/utils.py:1`.
