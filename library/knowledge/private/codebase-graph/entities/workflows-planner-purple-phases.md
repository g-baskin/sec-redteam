---
type: entity
title: "_purple_phases (workflows/planner.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: function
path: "src/sec_redteam/workflows/planner.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPhase]]"
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-module]]"
sources:
  - "src/sec_redteam/workflows/planner.py:86-118"
---

# _purple_phases (workflows/planner.py)

## Overview

Returns three fixed WorkflowPhase values: Joint Planning, Live Exercise, and Hardening Sprint. `src/sec_redteam/workflows/planner.py:86`

## Signature / Definition

```python
def _purple_phases(scenario: str) -> list[WorkflowPhase]:
```

`src/sec_redteam/workflows/planner.py:86-118`.

## Behavior

- Returns three fixed WorkflowPhase values: Joint Planning, Live Exercise, and Hardening Sprint. `src/sec_redteam/workflows/planner.py:86`
- Interpolates the scenario into the joint-planning action text. `src/sec_redteam/workflows/planner.py:92`

## Connections

- calls [[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPhase]] — `src/sec_redteam/workflows/planner.py:88`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]] (calls) — `src/sec_redteam/workflows/planner.py:153`.
- Declared in [[library/knowledge/private/codebase-graph/entities/workflows-planner-module]] — `src/sec_redteam/workflows/planner.py:86-118`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/planner.py:86-118`.
