---
type: entity
title: "domain_of (ingest/utils.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: function
path: "src/sec_redteam/ingest/utils.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-domain-allowed]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-module]]"
  - "[[library/knowledge/private/codebase-graph/concepts/corpus-filter-and-budget]]"
sources:
  - "src/sec_redteam/ingest/utils.py:10-13"
---

# domain_of (ingest/utils.py)

## Overview

Uses tldextract and joins only the extracted domain and suffix; subdomains are not preserved. `src/sec_redteam/ingest/utils.py:11`

## Signature / Definition

```python
def domain_of(url: str) -> str:
```

`src/sec_redteam/ingest/utils.py:10-13`.

## Behavior

- Uses tldextract and joins only the extracted domain and suffix; subdomains are not preserved. `src/sec_redteam/ingest/utils.py:11`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-domain-allowed]] (calls) — `src/sec_redteam/ingest/pipeline.py:67`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] (calls) — `src/sec_redteam/ingest/pipeline.py:133`.
- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-utils-module]] — `src/sec_redteam/ingest/utils.py:10-13`.
- [[library/knowledge/private/codebase-graph/concepts/corpus-filter-and-budget]] — `src/sec_redteam/ingest/utils.py:10-13`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/utils.py:10-13`.
