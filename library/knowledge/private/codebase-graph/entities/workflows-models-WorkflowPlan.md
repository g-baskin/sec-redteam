---
type: entity
title: "WorkflowPlan (workflows/models.py)"
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
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-module]]"
  - "[[library/knowledge/private/codebase-graph/concepts/evidence-is-attachment]]"
sources:
  - "src/sec_redteam/workflows/models.py:27-34"
schema_library: dataclasses
fields:
  - "workflow_type"
  - "scenario"
  - "scope"
  - "assumptions"
  - "phases"
  - "scorecard"
  - "evidence_sources"
---

# WorkflowPlan (workflows/models.py)

## Overview

Frozen, slotted dataclass combining workflow_type, scenario, scope, assumptions, phases, scorecard and evidence_sources. `src/sec_redteam/workflows/models.py:26`

## Signature / Definition

```python
class WorkflowPlan:
    workflow_type: WorkflowType
    scenario: str
    scope: str
    assumptions: list[str]
    phases: list[WorkflowPhase]
    scorecard: list[str]
    evidence_sources: list[EvidenceSource]
```

`src/sec_redteam/workflows/models.py:27-34`.

## Behavior

- Frozen, slotted dataclass combining workflow_type, scenario, scope, assumptions, phases, scorecard and evidence_sources. `src/sec_redteam/workflows/models.py:26`
- Its list-valued fields remain lists; frozen does not make their contents deeply immutable. `src/sec_redteam/workflows/models.py:31`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]] (calls) — `src/sec_redteam/workflows/planner.py:164`.
- Declared in [[library/knowledge/private/codebase-graph/entities/workflows-models-module]] — `src/sec_redteam/workflows/models.py:27-34`.
- [[library/knowledge/private/codebase-graph/concepts/evidence-is-attachment]] — `src/sec_redteam/workflows/models.py:27-34`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/models.py:27-34`.
