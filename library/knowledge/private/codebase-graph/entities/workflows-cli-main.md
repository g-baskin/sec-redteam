---
type: entity
title: "main (workflows/cli.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: function
path: "src/sec_redteam/workflows/cli.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-build-parser]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]]"
used_by: []
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-module]]"
  - "[[library/knowledge/private/codebase-graph/concepts/evidence-is-attachment]]"
sources:
  - "src/sec_redteam/workflows/cli.py:23-38"
---

# main (workflows/cli.py)

## Overview

Fetches evidence from the selected SQLite database. `src/sec_redteam/workflows/cli.py:26`

## Signature / Definition

```python
def main() -> None:
```

`src/sec_redteam/workflows/cli.py:23-38`.

## Behavior

- Fetches evidence from the selected SQLite database. `src/sec_redteam/workflows/cli.py:26`
- Passes evidence, scenario and scope to the fixed planner, then prints the dataclass as indented JSON. `src/sec_redteam/workflows/cli.py:32`

## Connections

- calls [[library/knowledge/private/codebase-graph/entities/workflows-cli-build-parser]] — `src/sec_redteam/workflows/cli.py:24`.
- calls [[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]] — `src/sec_redteam/workflows/cli.py:26`.
- calls [[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]] — `src/sec_redteam/workflows/cli.py:32`.
- Declared in [[library/knowledge/private/codebase-graph/entities/workflows-cli-module]] — `src/sec_redteam/workflows/cli.py:23-38`.
- [[library/knowledge/private/codebase-graph/concepts/evidence-is-attachment]] — `src/sec_redteam/workflows/cli.py:23-38`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/cli.py:23-38`.
