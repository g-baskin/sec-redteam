---
type: entity
title: "_domain_allowed (ingest/pipeline.py)"
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
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-domain-of]]"
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
  - "[[library/knowledge/private/codebase-graph/concepts/corpus-filter-and-budget]]"
sources:
  - "src/sec_redteam/ingest/pipeline.py:64-67"
---

# _domain_allowed (ingest/pipeline.py)

## Overview

An empty allowlist permits any URL; otherwise tests domain_of(url) for exact membership in the configured set. `src/sec_redteam/ingest/pipeline.py:65`

## Signature / Definition

```python
def _domain_allowed(url: str, allowed_domains: frozenset[str]) -> bool:
```

`src/sec_redteam/ingest/pipeline.py:64-67`.

## Behavior

- An empty allowlist permits any URL; otherwise tests domain_of(url) for exact membership in the configured set. `src/sec_redteam/ingest/pipeline.py:65`

## Connections

- calls [[library/knowledge/private/codebase-graph/entities/ingest-utils-domain-of]] — `src/sec_redteam/ingest/pipeline.py:67`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] (calls) — `src/sec_redteam/ingest/pipeline.py:116`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]] — `src/sec_redteam/ingest/pipeline.py:64-67`.
- [[library/knowledge/private/codebase-graph/concepts/corpus-filter-and-budget]] — `src/sec_redteam/ingest/pipeline.py:64-67`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/pipeline.py:64-67`.
