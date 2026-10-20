---
type: entity
title: "workflows/models.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/workflows/models.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-__init__-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-module]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-EvidenceSource]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPhase]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPlan]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowType]]"
sources:
  - "src/sec_redteam/workflows/models.py:1"
exports:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-EvidenceSource]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPhase]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPlan]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowType]]"
imports: []
---

# workflows/models.py

## Overview

Workflow type alias and phase, evidence and plan dataclasses. `src/sec_redteam/workflows/models.py:1`

## Signature / Definition

Source module: `src/sec_redteam/workflows/models.py:1`.

Declarations (one entity per linked page):
- [[library/knowledge/private/codebase-graph/entities/workflows-models-EvidenceSource]] — `src/sec_redteam/workflows/models.py:18-23`.
- [[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPhase]] — `src/sec_redteam/workflows/models.py:10-14`.
- [[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPlan]] — `src/sec_redteam/workflows/models.py:27-34`.
- [[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowType]] — `src/sec_redteam/workflows/models.py:6`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/workflows/models.py:1`.

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-__init__-module]] (imports) — `src/sec_redteam/workflows/__init__.py:1`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-cli-module]] (imports) — `src/sec_redteam/workflows/cli.py:9`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-evidence-module]] (imports) — `src/sec_redteam/workflows/evidence.py:7`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-planner-module]] (imports) — `src/sec_redteam/workflows/planner.py:3`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-models-EvidenceSource]] — `src/sec_redteam/workflows/models.py:18-23`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPhase]] — `src/sec_redteam/workflows/models.py:10-14`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPlan]] — `src/sec_redteam/workflows/models.py:27-34`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowType]] — `src/sec_redteam/workflows/models.py:6`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/models.py:1`.
