---
type: entity
title: "ingest/pipeline.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/ingest/pipeline.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-types-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-module]]"
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-__init__-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-module]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-ChunkedDocument]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-domain-allowed]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-extract-best-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-load-queries]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-looks-like-html]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
sources:
  - "src/sec_redteam/ingest/pipeline.py:1"
exports:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-ChunkedDocument]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
imports:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-types-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-module]]"
---

# ingest/pipeline.py

## Overview

Document chunk model and ingestion orchestration declarations. `src/sec_redteam/ingest/pipeline.py:1`

## Signature / Definition

Source module: `src/sec_redteam/ingest/pipeline.py:1`.

Declarations (one entity per linked page):
- [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-ChunkedDocument]] — `src/sec_redteam/ingest/pipeline.py:22-32`.
- [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-domain-allowed]] — `src/sec_redteam/ingest/pipeline.py:64-67`.
- [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-extract-best-text]] — `src/sec_redteam/ingest/pipeline.py:44-51`.
- [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-load-queries]] — `src/sec_redteam/ingest/pipeline.py:54-61`.
- [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-looks-like-html]] — `src/sec_redteam/ingest/pipeline.py:38-41`.
- [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] — `src/sec_redteam/ingest/pipeline.py:70-181`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/ingest/pipeline.py:1`.

## Connections

- imports [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]] — `src/sec_redteam/ingest/pipeline.py:13`.
- imports [[library/knowledge/private/codebase-graph/entities/ingest-storage-module]] — `src/sec_redteam/ingest/pipeline.py:14`.
- imports [[library/knowledge/private/codebase-graph/entities/ingest-types-module]] — `src/sec_redteam/ingest/pipeline.py:15`.
- imports [[library/knowledge/private/codebase-graph/entities/ingest-utils-module]] — `src/sec_redteam/ingest/pipeline.py:16`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-__init__-module]] (imports) — `src/sec_redteam/ingest/__init__.py:1`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-cli-module]] (imports) — `src/sec_redteam/ingest/cli.py:8`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-ChunkedDocument]] — `src/sec_redteam/ingest/pipeline.py:22-32`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-domain-allowed]] — `src/sec_redteam/ingest/pipeline.py:64-67`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-extract-best-text]] — `src/sec_redteam/ingest/pipeline.py:44-51`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-load-queries]] — `src/sec_redteam/ingest/pipeline.py:54-61`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-looks-like-html]] — `src/sec_redteam/ingest/pipeline.py:38-41`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] — `src/sec_redteam/ingest/pipeline.py:70-181`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/pipeline.py:1`.
