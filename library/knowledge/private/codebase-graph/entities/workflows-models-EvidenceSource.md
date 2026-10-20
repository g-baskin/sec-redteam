---
type: entity
title: "EvidenceSource (workflows/models.py)"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "entity"
  - "codebase-graph"
entity_type: data-model
path: "src/sec_redteam/workflows/models.py"
language: py
last_commit_hash: "1e71d28b23881f5d1c76849003cd144cfe545947"
depends_on: []
used_by:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]]"
tested_by: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-module]]"
  - "[[library/knowledge/private/codebase-graph/concepts/evidence-is-attachment]]"
sources:
  - "src/sec_redteam/workflows/models.py:18-23"
schema_library: dataclasses
fields:
  - "title"
  - "url"
  - "domain"
  - "topic"
  - "excerpt"
---

# EvidenceSource (workflows/models.py)

## Overview

Frozen, slotted dataclass storing title, url, domain, topic and excerpt. `src/sec_redteam/workflows/models.py:17`

## Signature / Definition

```python
class EvidenceSource:
    title: str
    url: str
    domain: str
    topic: str
    excerpt: str
```

`src/sec_redteam/workflows/models.py:18-23`.

## Behavior

- Frozen, slotted dataclass storing title, url, domain, topic and excerpt. `src/sec_redteam/workflows/models.py:17`

## Connections

- Referenced by [[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]] (calls) — `src/sec_redteam/workflows/evidence.py:53`.
- Declared in [[library/knowledge/private/codebase-graph/entities/workflows-models-module]] — `src/sec_redteam/workflows/models.py:18-23`.
- [[library/knowledge/private/codebase-graph/concepts/evidence-is-attachment]] — `src/sec_redteam/workflows/models.py:18-23`.

## Tested by

Tests are outside this scan; no test coverage claim is made.

## History

Last file commit: `1e71d28b23881f5d1c76849003cd144cfe545947` (2026-10-19), `chore: publish AGPL-3.0-only source baseline`; read using `git log -- src/sec_redteam`. Source bytes match HEAD; see [source receipt](../meta/source-receipt.json). No earlier design history is inferred.

## Sources

- `src/sec_redteam/workflows/models.py:18-23`.
