---
type: entity
title: "build_parser (workflows/cli.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: function
path: "src/sec_redteam/workflows/cli.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-main]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-module]]"
sources:
  - "src/sec_redteam/workflows/cli.py:13-20"
---

# build_parser (workflows/cli.py)

## Overview

Restricts CLI workflow types to red, blue or purple and requires --scenario. `src/sec_redteam/workflows/cli.py:15`

## Signature / Definition

```python
def build_parser() -> argparse.ArgumentParser:
```

`src/sec_redteam/workflows/cli.py:13-20`.

## Behavior

- Restricts CLI workflow types to red, blue or purple and requires --scenario. `src/sec_redteam/workflows/cli.py:15`
- Defaults scope to lab, database to data/cyber_corpus.db and evidence limit to 10. `src/sec_redteam/workflows/cli.py:17`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-cli-main]] (calls) — `src/sec_redteam/workflows/cli.py:24`.
- Declared in [[library/knowledge/private/codebase-graph/entities/workflows-cli-module]] — `src/sec_redteam/workflows/cli.py:13-20`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/cli.py:13-20`.
