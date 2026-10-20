---
type: entity
title: "PRESETS (ingest/presets.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: exported-symbol
path: "src/sec_redteam/ingest/presets.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by: []
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-presets-module]]"
sources:
  - "src/sec_redteam/ingest/presets.py:15-64"
symbol_kind: object
is_default_export: false
---

# PRESETS (ingest/presets.py)

## Overview

Maps eight named profiles to IngestPreset values. `src/sec_redteam/ingest/presets.py:15`

## Signature / Definition

```python
PRESETS: dict[str, IngestPreset]  # registry declared at line 15
```

`src/sec_redteam/ingest/presets.py:15-64`.

## Behavior

- Maps eight named profiles to IngestPreset values. `src/sec_redteam/ingest/presets.py:15`
- Query paths are repository-working-directory-relative, not computed from the installed module location. `src/sec_redteam/ingest/presets.py:17`
- offsec-research and max-coverage use the same query filename but different numeric settings. `src/sec_redteam/ingest/presets.py:28`

## Connections

- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-presets-module]] — `src/sec_redteam/ingest/presets.py:15-64`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/presets.py:15-64`.
