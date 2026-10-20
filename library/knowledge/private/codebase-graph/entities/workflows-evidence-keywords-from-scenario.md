---
type: entity
title: "_keywords_from_scenario (workflows/evidence.py)"
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
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-module]]"
sources:
  - "src/sec_redteam/workflows/evidence.py:10-16"
---

# _keywords_from_scenario (workflows/evidence.py)

## Overview

Extracts lowercased ASCII alphanumeric tokens of at least four characters. `src/sec_redteam/workflows/evidence.py:11`

## Signature / Definition

```python
def _keywords_from_scenario(scenario: str) -> list[str]:
```

`src/sec_redteam/workflows/evidence.py:10-16`.

## Behavior

- Extracts lowercased ASCII alphanumeric tokens of at least four characters. `src/sec_redteam/workflows/evidence.py:11`
- Preserves first-occurrence order while deduplicating, retaining at most eight keywords. `src/sec_redteam/workflows/evidence.py:13`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]] (calls) — `src/sec_redteam/workflows/evidence.py:23`.
- Declared in [[library/knowledge/private/codebase-graph/entities/workflows-evidence-module]] — `src/sec_redteam/workflows/evidence.py:10-16`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/evidence.py:10-16`.
