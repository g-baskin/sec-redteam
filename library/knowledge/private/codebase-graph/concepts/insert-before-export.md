---
type: concept
title: "Insert before export"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "concept"
  - "codebase-graph"
complexity: intermediate
domain: codebase-graph
aliases: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-insert-doc]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-chunk-text]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-storage-DocumentRecord]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-ChunkedDocument]]"
sources:
  - "src/sec_redteam/ingest/pipeline.py:22-32"
  - "src/sec_redteam/ingest/pipeline.py:70-181"
  - "src/sec_redteam/ingest/storage.py:49-75"
  - "src/sec_redteam/ingest/storage.py:9-20"
  - "src/sec_redteam/ingest/utils.py:25-41"
---

# Insert before export

## Definition

SQLite persistence precedes JSONL chunk creation rather than sharing an atomic transaction. `src/sec_redteam/ingest/storage.py:72`; `src/sec_redteam/ingest/pipeline.py:141-160`.

## How it works

1. The record stores full text and its content hash. `src/sec_redteam/ingest/storage.py:9-20`.
2. Insertion commits before returning True; uniqueness conflicts return False. `src/sec_redteam/ingest/storage.py:49-75`.
3. Only then does the pipeline validate/slice chunks and append JSONL. `src/sec_redteam/ingest/pipeline.py:141-160`; `src/sec_redteam/ingest/utils.py:25-41`.

## Why it matters

A chunk-validation or output-write failure can leave a committed row without a matching export. Rerunning skips duplicate rows, so changing the JSONL destination or chunk settings does not regenerate previously stored documents. This is a consequence of the branch and commit order, not a tested recovery guarantee. `src/sec_redteam/ingest/storage.py:72-75`; `src/sec_redteam/ingest/pipeline.py:141-160`.

## Examples and connections

- [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] — `src/sec_redteam/ingest/pipeline.py:70-181`.
- [[library/knowledge/private/codebase-graph/entities/ingest-storage-insert-doc]] — `src/sec_redteam/ingest/storage.py:49-75`.
- [[library/knowledge/private/codebase-graph/entities/ingest-utils-chunk-text]] — `src/sec_redteam/ingest/utils.py:25-41`.
- [[library/knowledge/private/codebase-graph/entities/ingest-storage-DocumentRecord]] — `src/sec_redteam/ingest/storage.py:9-20`.
- [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-ChunkedDocument]] — `src/sec_redteam/ingest/pipeline.py:22-32`.

## Sources

- `src/sec_redteam/ingest/pipeline.py:70-181`.
- `src/sec_redteam/ingest/storage.py:49-75`.
- `src/sec_redteam/ingest/utils.py:25-41`.
- `src/sec_redteam/ingest/storage.py:9-20`.
- `src/sec_redteam/ingest/pipeline.py:22-32`.
