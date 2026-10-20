---
type: entity
title: "workflows/__init__.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/workflows/__init__.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-module]]"
used_by: []
tested_by: []
related: []
sources:
  - "src/sec_redteam/workflows/__init__.py:1"
exports: []
imports:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-module]]"
---

# workflows/__init__.py

## Overview

Re-export surface for WorkflowPlan, WorkflowType and build_workflow_plan. `src/sec_redteam/workflows/__init__.py:1`

## Signature / Definition

Source module: `src/sec_redteam/workflows/__init__.py:1`.

```python
from .models import WorkflowPlan, WorkflowType
from .planner import build_workflow_plan

__all__ = ["WorkflowPlan", "WorkflowType", "build_workflow_plan"]
```

`src/sec_redteam/workflows/__init__.py:1`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/workflows/__init__.py:1`.

## Connections

- imports [[library/knowledge/private/codebase-graph/entities/workflows-models-module]] — `src/sec_redteam/workflows/__init__.py:1`.
- imports [[library/knowledge/private/codebase-graph/entities/workflows-planner-module]] — `src/sec_redteam/workflows/__init__.py:2`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/__init__.py:1`.
