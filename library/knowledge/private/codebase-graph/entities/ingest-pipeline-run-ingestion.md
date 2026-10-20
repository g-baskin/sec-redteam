---
type: entity
title: "run_ingestion (ingest/pipeline.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: function
path: "src/sec_redteam/ingest/pipeline.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-ChunkedDocument]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-domain-allowed]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-extract-best-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-load-queries]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-DocumentRecord]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-init-db]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-insert-doc]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-chunk-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-domain-of]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-normalize-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-sha256-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-sort-deterministic]]"
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-main]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
  - "[[library/knowledge/private/codebase-graph/concepts/insert-before-export]]"
  - "[[library/knowledge/private/codebase-graph/concepts/corpus-filter-and-budget]]"
sources:
  - "src/sec_redteam/ingest/pipeline.py:70-181"
---

# run_ingestion (ingest/pipeline.py)

## Overview

Loads queries, initializes SQLite and opens JSONL in append mode. `src/sec_redteam/ingest/pipeline.py:72`

## Signature / Definition

```python
def run_ingestion(settings: IngestionSettings, client: SearchClient) -> int:
```

`src/sec_redteam/ingest/pipeline.py:70-181`.

## Behavior

- Loads queries, initializes SQLite and opens JSONL in append mode. `src/sec_redteam/ingest/pipeline.py:72`
- Processes topics and queries in sorted order; catches search exceptions and continues without the normal inter-call delay. `src/sec_redteam/ingest/pipeline.py:81`
- Counts every returned result toward estimated spend; a batch reaching or exceeding the budget is discarded before storage. `src/sec_redteam/ingest/pipeline.py:100`
- Filters missing, seen and disallowed URLs, then marks a URL seen before checking cleaned text length. `src/sec_redteam/ingest/pipeline.py:113`
- Uses a current UTC fetch time, a SHA-256 content hash, and the first 24 hex characters of the URL hash as the document ID. `src/sec_redteam/ingest/pipeline.py:124`
- Only newly inserted rows reach chunking and JSONL output; the SQLite commit precedes both operations. `src/sec_redteam/ingest/pipeline.py:141-160`; `src/sec_redteam/ingest/storage.py:72`
- Sleeps after successful query processing; returns the number of JSONL records written at line 181. `src/sec_redteam/ingest/pipeline.py:166`

## Connections

- calls [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-ChunkedDocument]] — `src/sec_redteam/ingest/pipeline.py:144`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-domain-allowed]] — `src/sec_redteam/ingest/pipeline.py:116`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-extract-best-text]] — `src/sec_redteam/ingest/pipeline.py:120`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-load-queries]] — `src/sec_redteam/ingest/pipeline.py:72`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-storage-DocumentRecord]] — `src/sec_redteam/ingest/pipeline.py:127`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-storage-init-db]] — `src/sec_redteam/ingest/pipeline.py:73`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-storage-insert-doc]] — `src/sec_redteam/ingest/pipeline.py:141`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-utils-chunk-text]] — `src/sec_redteam/ingest/pipeline.py:154`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-utils-domain-of]] — `src/sec_redteam/ingest/pipeline.py:133`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-utils-normalize-text]] — `src/sec_redteam/ingest/pipeline.py:120`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-utils-sha256-text]] — `src/sec_redteam/ingest/pipeline.py:125`.
- calls [[library/knowledge/private/codebase-graph/entities/ingest-utils-sort-deterministic]] — `src/sec_redteam/ingest/pipeline.py:81`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-cli-main]] (calls) — `src/sec_redteam/ingest/cli.py:88`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]] — `src/sec_redteam/ingest/pipeline.py:70-181`.
- [[library/knowledge/private/codebase-graph/concepts/insert-before-export]] — `src/sec_redteam/ingest/pipeline.py:70-181`.
- [[library/knowledge/private/codebase-graph/concepts/corpus-filter-and-budget]] — `src/sec_redteam/ingest/pipeline.py:70-181`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/pipeline.py:70-181`.
