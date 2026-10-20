---
type: entity
title: "workflows/cli.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/workflows/cli.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-module]]"
used_by: []
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-build-parser]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-main]]"
sources:
  - "src/sec_redteam/workflows/cli.py:1"
exports:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-build-parser]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-main]]"
imports:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-module]]"
---

# workflows/cli.py

## Overview

Argument-parsing entry point wiring evidence lookup and plan serialization. `src/sec_redteam/workflows/cli.py:1`

## Signature / Definition

Source module: `src/sec_redteam/workflows/cli.py:1`.

Declarations (one entity per linked page):
- [[library/knowledge/private/codebase-graph/entities/workflows-cli-build-parser]] — `src/sec_redteam/workflows/cli.py:13-20`.
- [[library/knowledge/private/codebase-graph/entities/workflows-cli-main]] — `src/sec_redteam/workflows/cli.py:23-38`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/workflows/cli.py:1`.

## Connections

- imports [[library/knowledge/private/codebase-graph/entities/workflows-evidence-module]] — `src/sec_redteam/workflows/cli.py:8`.
- imports [[library/knowledge/private/codebase-graph/entities/workflows-models-module]] — `src/sec_redteam/workflows/cli.py:9`.
- imports [[library/knowledge/private/codebase-graph/entities/workflows-planner-module]] — `src/sec_redteam/workflows/cli.py:10`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-cli-build-parser]] — `src/sec_redteam/workflows/cli.py:13-20`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-cli-main]] — `src/sec_redteam/workflows/cli.py:23-38`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/cli.py:1`.
