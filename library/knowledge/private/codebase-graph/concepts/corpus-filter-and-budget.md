---
type: concept
title: "Corpus filtering and estimated budget boundaries"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - "concept"
  - "codebase-graph"
complexity: intermediate
domain: codebase-graph
aliases: []
related:
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-main]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-cli-DEFAULT-ALLOWED-DOMAINS]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-domain-allowed]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]]"
  - "[[library/knowledge/private/codebase-graph/entities/ingest-utils-domain-of]]"
sources:
  - "src/sec_redteam/ingest/cli.py:12-24"
  - "src/sec_redteam/ingest/cli.py:64-88"
  - "src/sec_redteam/ingest/pipeline.py:64-67"
  - "src/sec_redteam/ingest/pipeline.py:70-181"
  - "src/sec_redteam/ingest/utils.py:10-13"
---

# Corpus filtering and estimated budget boundaries

## Definition

The ingestion allowlist filters corpus results, while the budget is estimated after a provider response. Neither is an exercise execution boundary. `src/sec_redteam/ingest/pipeline.py:86-118`.

## How it works

1. Explicit CLI allow-domain values replace the default set. `src/sec_redteam/ingest/cli.py:72`.
2. URL normalization retains the extracted domain and suffix but drops subdomains. `src/sec_redteam/ingest/utils.py:10-13`.
3. Empty allowlists permit every URL; otherwise normalized domains must exactly match an entry. `src/sec_redteam/ingest/pipeline.py:64-67`.
4. The estimate counts every returned result before filtering or deduplication. A batch reaching the cap is discarded. `src/sec_redteam/ingest/pipeline.py:100-118`.

## Why it matters

Default cloud-provider subdomain entries do not match their normalized registrable domains as written. The post-fetch estimate cannot impose a hard provider spending limit. `src/sec_redteam/ingest/cli.py:20-22`; `src/sec_redteam/ingest/utils.py:11-13`; `src/sec_redteam/ingest/pipeline.py:86-111`.

## Examples and connections

- [[library/knowledge/private/codebase-graph/entities/ingest-cli-main]] — `src/sec_redteam/ingest/cli.py:64-88`.
- [[library/knowledge/private/codebase-graph/entities/ingest-cli-DEFAULT-ALLOWED-DOMAINS]] — `src/sec_redteam/ingest/cli.py:12-24`.
- [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-domain-allowed]] — `src/sec_redteam/ingest/pipeline.py:64-67`.
- [[library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion]] — `src/sec_redteam/ingest/pipeline.py:70-181`.
- [[library/knowledge/private/codebase-graph/entities/ingest-utils-domain-of]] — `src/sec_redteam/ingest/utils.py:10-13`.

## Sources

- `src/sec_redteam/ingest/cli.py:64-88`.
- `src/sec_redteam/ingest/cli.py:12-24`.
- `src/sec_redteam/ingest/pipeline.py:64-67`.
- `src/sec_redteam/ingest/pipeline.py:70-181`.
- `src/sec_redteam/ingest/utils.py:10-13`.
