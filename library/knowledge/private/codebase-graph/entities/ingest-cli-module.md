---
type: entity
title: "ingest/cli.py"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: module
path: "src/sec_redteam/ingest/cli.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-presets-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-types-module]]"
used_by: []
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-DEFAULT-ALLOWED-DOMAINS]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-build-parser]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-main]]"
sources:
  - "src/sec_redteam/ingest/cli.py:1"
exports:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-DEFAULT-ALLOWED-DOMAINS]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-build-parser]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-main]]"
imports:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-presets-module]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-types-module]]"
---

# ingest/cli.py

## Overview

Argument-parsing entry point wiring presets, settings, the Exa adapter and ingestion. `src/sec_redteam/ingest/cli.py:1`

## Signature / Definition

Source module: `src/sec_redteam/ingest/cli.py:1`.

Declarations (one entity per linked page):
- [[library/knowledge/private/codebase-graph/entities/ingest-cli-DEFAULT-ALLOWED-DOMAINS]] — `src/sec_redteam/ingest/cli.py:12-24`.
- [[library/knowledge/private/codebase-graph/entities/ingest-cli-build-parser]] — `src/sec_redteam/ingest/cli.py:27-61`.
- [[library/knowledge/private/codebase-graph/entities/ingest-cli-main]] — `src/sec_redteam/ingest/cli.py:64-88`.

## Behavior

This page is a declaration map; behavior is documented on the linked atomic pages above. `src/sec_redteam/ingest/cli.py:1`.

## Connections

- imports [[library/knowledge/private/codebase-graph/entities/ingest-exa_client-module]] — `src/sec_redteam/ingest/cli.py:7`.
- imports [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-module]] — `src/sec_redteam/ingest/cli.py:8`.
- imports [[library/knowledge/private/codebase-graph/entities/ingest-presets-module]] — `src/sec_redteam/ingest/cli.py:9`.
- imports [[library/knowledge/private/codebase-graph/entities/ingest-types-module]] — `src/sec_redteam/ingest/cli.py:10`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-cli-DEFAULT-ALLOWED-DOMAINS]] — `src/sec_redteam/ingest/cli.py:12-24`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-cli-build-parser]] — `src/sec_redteam/ingest/cli.py:27-61`.
- Declares [[library/knowledge/private/codebase-graph/entities/ingest-cli-main]] — `src/sec_redteam/ingest/cli.py:64-88`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/cli.py:1`.
