---
type: entity
title: "workflows/evidence.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/workflows/evidence.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-module]]"
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-module]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-keywords-from-scenario]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]]"
sources:
  - "src/sec_redteam/workflows/evidence.py:1"
exports:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]]"
imports:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-module]]"
---

# workflows/evidence.py

## Overview

Scenario keyword extraction and SQLite evidence selection functions. `src/sec_redteam/workflows/evidence.py:1`

## Signature / Definition

Source module: `src/sec_redteam/workflows/evidence.py:1`.

Declarations (one entity per linked page):
- [[library/knowledge/private/codebase-graph/entities/workflows-evidence-keywords-from-scenario]] — `src/sec_redteam/workflows/evidence.py:10-16`.
- [[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]] — `src/sec_redteam/workflows/evidence.py:19-61`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/workflows/evidence.py:1`.

## Connections

- imports [[library/knowledge/private/codebase-graph/entities/workflows-models-module]] — `src/sec_redteam/workflows/evidence.py:7`.
- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-cli-module]] (imports) — `src/sec_redteam/workflows/cli.py:8`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-evidence-keywords-from-scenario]] — `src/sec_redteam/workflows/evidence.py:10-16`.
- Declares [[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]] — `src/sec_redteam/workflows/evidence.py:19-61`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/evidence.py:1`.
