---
type: entity
title: "ingest/presets.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/ingest/presets.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-module]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-presets-IngestPreset]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-presets-PRESETS]]"
sources:
  - "src/sec_redteam/ingest/presets.py:1"
exports:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-presets-IngestPreset]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-presets-PRESETS]]"
imports: []
---

# ingest/presets.py

## Overview

Preset model and named ingestion-profile registry. `src/sec_redteam/ingest/presets.py:1`

## Signature / Definition

Source module: `src/sec_redteam/ingest/presets.py:1`.

Declarations (one entity per linked page):
- [[library/knowledge/private/codebase-graph/entities/ingest-presets-IngestPreset]] — `src/sec_redteam/ingest/presets.py:8-12`.
- [[library/knowledge/private/codebase-graph/entities/ingest-presets-PRESETS]] — `src/sec_redteam/ingest/presets.py:15-64`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/ingest/presets.py:1`.

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/ingest-cli-module]] (imports) — `src/sec_redteam/ingest/cli.py:9`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-presets-IngestPreset]] — `src/sec_redteam/ingest/presets.py:8-12`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-presets-PRESETS]] — `src/sec_redteam/ingest/presets.py:15-64`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/presets.py:1`.
