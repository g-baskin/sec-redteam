---
type: entity
title: "WorkflowPhase (workflows/models.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: data-model
path: "src/sec_redteam/workflows/models.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-blue-phases]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-purple-phases]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-red-phases]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-module]]"
sources:
  - "src/sec_redteam/workflows/models.py:10-14"
schema_library: dataclasses
fields:
  - "name"
  - "objective"
  - "actions"
  - "outputs"
---

# WorkflowPhase (workflows/models.py)

## Overview

Frozen, slotted dataclass storing name, objective, actions and outputs; actions and outputs are lists of strings. `src/sec_redteam/workflows/models.py:9`

## Signature / Definition

```python
class WorkflowPhase:
    name: str
    objective: str
    actions: list[str]
    outputs: list[str]
```

`src/sec_redteam/workflows/models.py:10-14`.

## Behavior

- Frozen, slotted dataclass storing name, objective, actions and outputs; actions and outputs are lists of strings. `src/sec_redteam/workflows/models.py:9`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-planner-blue-phases]] (calls) — `src/sec_redteam/workflows/planner.py:53`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-planner-purple-phases]] (calls) — `src/sec_redteam/workflows/planner.py:88`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-planner-red-phases]] (calls) — `src/sec_redteam/workflows/planner.py:8`.
- Declared in [[library/knowledge/private/codebase-graph/entities/workflows-models-module]] — `src/sec_redteam/workflows/models.py:10-14`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/models.py:10-14`.
