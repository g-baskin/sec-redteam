---
type: entity
title: "DEFAULT_ALLOWED_DOMAINS (ingest/cli.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: exported-symbol
path: "src/sec_redteam/ingest/cli.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by: []
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-module]]"
  - "[[library/knowledge/private/codebase-graph/concepts/corpus-filter-and-budget]]"
sources:
  - "src/sec_redteam/ingest/cli.py:12-24"
symbol_kind: object
is_default_export: false
---

# DEFAULT_ALLOWED_DOMAINS (ingest/cli.py)

## Overview

A frozenset containing nine default domain strings, including cloud-provider subdomains. `src/sec_redteam/ingest/cli.py:12`

## Signature / Definition

```python
DEFAULT_ALLOWED_DOMAINS = frozenset(
    {
        "mitre.org",
        "owasp.org",
        "nist.gov",
        "cisa.gov",
        "sans.org",
        "github.com",
        "cloud.google.com",
        "learn.microsoft.com",
        "aws.amazon.com",
    }
)
```

`src/sec_redteam/ingest/cli.py:12-24`.

## Behavior

- A frozenset containing nine default domain strings, including cloud-provider subdomains. `src/sec_redteam/ingest/cli.py:12`
- main replaces this set when explicit allow-domain values are supplied. `src/sec_redteam/ingest/cli.py:72`

## Connections

- Declared in [[library/knowledge/private/codebase-graph/entities/ingest-cli-module]] — `src/sec_redteam/ingest/cli.py:12-24`.
- [[library/knowledge/private/codebase-graph/concepts/corpus-filter-and-budget]] — `src/sec_redteam/ingest/cli.py:12-24`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/ingest/cli.py:12-24`.
