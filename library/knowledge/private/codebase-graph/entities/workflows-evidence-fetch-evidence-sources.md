---
type: entity
title: "fetch_evidence_sources (workflows/evidence.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: function
path: "src/sec_redteam/workflows/evidence.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-keywords-from-scenario]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-EvidenceSource]]"
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-main]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-module]]"
  - "[[library/knowledge/private/codebase-graph/concepts/evidence-is-attachment]]"
sources:
  - "src/sec_redteam/workflows/evidence.py:19-61"
---

# fetch_evidence_sources (workflows/evidence.py)

## Overview

Returns an empty list when the database path does not exist. `src/sec_redteam/workflows/evidence.py:20`

## Signature / Definition

```python
def fetch_evidence_sources(db_path: Path, scenario: str, workflow_type: str, limit: int = 10) -> list[EvidenceSource]:
```

`src/sec_redteam/workflows/evidence.py:19-61`.

## Behavior

- Returns an empty list when the database path does not exist. `src/sec_redteam/workflows/evidence.py:20`
- Uses scenario keywords or falls back to the workflow type. `src/sec_redteam/workflows/evidence.py:23`
- OR-combines parameterized substring LIKE matches across title, text and topic. `src/sec_redteam/workflows/evidence.py:27`
- Reads docs, takes the first 280 text characters and orders by rowid descending; this is insertion recency, not relevance scoring. `src/sec_redteam/workflows/evidence.py:35`
- Opens SQLite and closes it in finally; query errors are not swallowed. `src/sec_redteam/workflows/evidence.py:44`
- Converts rows to EvidenceSource values with empty-string fallbacks. `src/sec_redteam/workflows/evidence.py:50`

## Connections

- calls [[library/knowledge/private/codebase-graph/entities/workflows-evidence-keywords-from-scenario]] — `src/sec_redteam/workflows/evidence.py:23`.
- calls [[library/knowledge/private/codebase-graph/entities/workflows-models-EvidenceSource]] — `src/sec_redteam/workflows/evidence.py:53`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-cli-main]] (calls) — `src/sec_redteam/workflows/cli.py:26`.
- Declared in [[library/knowledge/private/codebase-graph/entities/workflows-evidence-module]] — `src/sec_redteam/workflows/evidence.py:19-61`.
- [[library/knowledge/private/codebase-graph/concepts/evidence-is-attachment]] — `src/sec_redteam/workflows/evidence.py:19-61`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/evidence.py:19-61`.
