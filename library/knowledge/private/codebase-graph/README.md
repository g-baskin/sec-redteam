---
type: meta
title: "Local codebase graph and atomic wiki"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - meta
  - codebase-graph
related: []
sources:
  - "library/knowledge/private/codebase-graph/meta/source-receipt.json"
---

# Local codebase graph and atomic wiki

Scope: `src/sec_redteam`. Source HEAD: `1e71d28b23881f5d1c76849003cd144cfe545947`.
This is a **local-only partial scan**, not a cloud snapshot or global wiki index.

## Artifacts

- [Graph JSON](graph.json): 58 extracted nodes and 87 directed edges across 14 Python files.
- [Source receipt](meta/source-receipt.json): source HEAD, 21 file hashes, tool version, isolation settings and normalized-graph checksum.
- [Extraction receipt](meta/extraction-receipt.md): actual checks and known limitations.
- [Structured response](meta/response-payload.json): complete page lists, detected entities and gaps; `partial_scan: true`.
- `entities/`: 49 extracted entity pages plus seven filename-only JSON stubs.
- `concepts/`: three source-cited concepts. Every Markdown page is below 300 lines.

## Start here

| Area | Atomic entry pages |
| --- | --- |
| Ingestion entry | [CLI module](entities/ingest-cli-module.md), [main](entities/ingest-cli-main.md), [settings](entities/ingest-types-IngestionSettings.md) |
| Search adapter | [module](entities/ingest-exa_client-module.md), [ExaSearchClient](entities/ingest-exa_client-ExaSearchClient.md), [SearchClient](entities/ingest-exa_client-SearchClient.md) |
| Ingestion flow | [pipeline module](entities/ingest-pipeline-module.md), [run_ingestion](entities/ingest-pipeline-run-ingestion.md) |
| Persistence | [storage module](entities/ingest-storage-module.md), [DocumentRecord](entities/ingest-storage-DocumentRecord.md), [insert_doc](entities/ingest-storage-insert-doc.md) |
| Utilities | [module](entities/ingest-utils-module.md), [chunk_text](entities/ingest-utils-chunk-text.md), [domain_of](entities/ingest-utils-domain-of.md) |
| Presets | [module](entities/ingest-presets-module.md), [PRESETS](entities/ingest-presets-PRESETS.md) |
| Workflow entry | [CLI module](entities/workflows-cli-module.md), [main](entities/workflows-cli-main.md) |
| Evidence | [module](entities/workflows-evidence-module.md), [fetch_evidence_sources](entities/workflows-evidence-fetch-evidence-sources.md) |
| Plans | [planner module](entities/workflows-planner-module.md), [build_workflow_plan](entities/workflows-planner-build-workflow-plan.md), [models](entities/workflows-models-module.md) |
| Package surfaces | [root](entities/__init__-module.md), [ingest](entities/ingest-__init__-module.md), [workflows](entities/workflows-__init__-module.md) |

Concepts:

- [Insert before export](concepts/insert-before-export.md).
- [Evidence is an attachment](concepts/evidence-is-attachment.md).
- [Corpus filtering and estimated budget](concepts/corpus-filter-and-budget.md).

JSON query-file stubs:
[default](entities/default_queries.md), [badass today](entities/badass_today_queries.md),
[offsec research](entities/offsec_research_queries.md), [aggressive breadth](entities/aggressive_breadth_queries.md),
[compliance surge](entities/compliance_surge_queries.md), [compliance deep](entities/compliance_deep_queries.md),
[playbook surge](entities/playbook_surge_queries.md).

## Reading the graph

`graph.json` uses node-link JSON: `nodes` contain declarations and file modules; `links` contain `source`, `target`, `relation` and the extractor's original `confidence` label. Internal IDs and `source_file` values are repository-relative. `source_location` uses one-based line coordinates.

Edges: 52 imports, 31 calls, three method ownership links and one inheritance link. Thirty-seven edges point outside the node set: 36 external-module imports and one unresolved `Protocol` inheritance target. Consumers must retain these as boundary references, not assume every endpoint has a declaration node. These counts are recorded in the receipts.

`EXTRACTED` means emitted by this extractor, not independently proved runtime behavior. `exported`, `is_entrypoint` and degree fields are extractor heuristics. Missing edges do not establish absence of a dependency. In particular, receiver calls such as `client.search_and_contents` are not resolved to implementations (`src/sec_redteam/ingest/pipeline.py:86`).

The wiki supplements declarations with source-read behavior and in-scope relationships; it does not add speculative edges to the graph. Three method nodes are described with their owning classes. Six incidental constants remain in JSON without separate pages. Query JSON files have stubs, not parsed entity graphs. Tests, dependencies and all files outside the named subtree are excluded.

## Isolation and refresh boundary

The installed Hivemind 0.7.161 CLI ran with an empty inherited environment, a disposable HOME, graph push/pull disabled, auto-doc registry redirected to `/dev/null`, and macOS `sandbox-exec` denying network access. The build reported cloud push disabled. No ingestion or plan CLI was executed; no credentials, `.env` or corpus data were read by this documentation task.

The normal graph command can push and auto-refresh docs: **do not rerun it without equivalent isolation**. Inspect the installed command's behavior again before refreshing. Retain the source receipt and compare prior contracts before replacing pages; contract changes require the four-artifact contradiction protocol. Do not silently overwrite history.

Machine observations, absolute worktree paths and the machine-derived repo key were omitted from the published graph. Keys, nodes and edges were sorted; source HEAD and hashes live in the separate receipt. No automatic hooks, native integration setup, upload, paid request, cloud sync, commit or push was performed.

This README is local navigation, not a driver-owned index. Global wiki indexes, logs, hash manifests and reconciliation remain untouched and are **not authorized** by this result's `partial_scan` flag.
