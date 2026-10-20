---
type: entity
title: "workflows/planner.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/workflows/planner.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-module]]"
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-__init__-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-module]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-blue-phases]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-purple-phases]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-red-phases]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]]"
sources:
  - "src/sec_redteam/workflows/planner.py:1"
exports:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]]"
imports:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-module]]"
---

# workflows/planner.py

## Overview

Fixed phase constructors and workflow-plan assembly function. `src/sec_redteam/workflows/planner.py:1`

## Signature / Definition

Source module: `src/sec_redteam/workflows/planner.py:1`.

Declarations (one entity per linked page):
- [[library/knowledge/private/codebase-graph/entities/workflows-planner-blue-phases]] — `src/sec_redteam/workflows/planner.py:51-83`.
- [[library/knowledge/private/codebase-graph/entities/workflows-planner-purple-phases]] — `src/sec_redteam/workflows/planner.py:86-118`.
- [[library/knowledge/private/codebase-graph/entities/workflows-planner-red-phases]] — `src/sec_redteam/workflows/planner.py:6-48`.
- [[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]] — `src/sec_redteam/workflows/planner.py:121-172`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/workflows/planner.py:1`.

## Connections

- imports [[library/knowledge/private/codebase-graph/entities/workflows-models-module]] — `src/sec_redteam/workflows/planner.py:3`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-__init__-module]] (imports) — `src/sec_redteam/workflows/__init__.py:2`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-cli-module]] (imports) — `src/sec_redteam/workflows/cli.py:10`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-planner-blue-phases]] — `src/sec_redteam/workflows/planner.py:51-83`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-planner-purple-phases]] — `src/sec_redteam/workflows/planner.py:86-118`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-planner-red-phases]] — `src/sec_redteam/workflows/planner.py:6-48`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]] — `src/sec_redteam/workflows/planner.py:121-172`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/planner.py:1`.
