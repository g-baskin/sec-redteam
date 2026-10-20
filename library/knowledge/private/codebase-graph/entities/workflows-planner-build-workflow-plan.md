---
type: entity
title: "build_workflow_plan (workflows/planner.py)"
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
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPlan]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-blue-phases]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-purple-phases]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-red-phases]]"
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-main]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-module]]"
  - "[[library/knowledge/private/codebase-graph/concepts/evidence-is-attachment]]"
sources:
  - "src/sec_redteam/workflows/planner.py:121-172"
---

# build_workflow_plan (workflows/planner.py)

## Overview

Strips the scenario, replacing an empty result with adversary simulation. `src/sec_redteam/workflows/planner.py:127`

## Signature / Definition

```python
def build_workflow_plan(
    workflow_type: WorkflowType,
    scenario: str,
    scope: str,
    evidence_sources: list[EvidenceSource] | None = None,
) -> WorkflowPlan:
```

`src/sec_redteam/workflows/planner.py:121-172`.

## Behavior

- Strips the scenario, replacing an empty result with adversary simulation. `src/sec_redteam/workflows/planner.py:127`
- Selects red or blue templates explicitly; every other runtime value falls into the purple branch at line 152. `src/sec_redteam/workflows/planner.py:128`
- Returns WorkflowPlan with scope copied verbatim and evidence_sources attached separately; evidence does not select or alter the phases. `src/sec_redteam/workflows/planner.py:164`
- Authorization assumptions are output strings, not runtime authorization checks. `src/sec_redteam/workflows/planner.py:130`

## Connections

- calls [[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPlan]] — `src/sec_redteam/workflows/planner.py:164`.
- calls [[library/knowledge/private/codebase-graph/entities/workflows-planner-blue-phases]] — `src/sec_redteam/workflows/planner.py:142`.
- calls [[library/knowledge/private/codebase-graph/entities/workflows-planner-purple-phases]] — `src/sec_redteam/workflows/planner.py:153`.
- calls [[library/knowledge/private/codebase-graph/entities/workflows-planner-red-phases]] — `src/sec_redteam/workflows/planner.py:129`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-cli-main]] (calls) — `src/sec_redteam/workflows/cli.py:32`.
- Declared in [[library/knowledge/private/codebase-graph/entities/workflows-planner-module]] — `src/sec_redteam/workflows/planner.py:121-172`.
- [[library/knowledge/private/codebase-graph/concepts/evidence-is-attachment]] — `src/sec_redteam/workflows/planner.py:121-172`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/planner.py:121-172`.
