---
type: meta
title: "Local graph extraction receipt"
created: "2026-10-19"
updated: "2026-10-19"
status: developing
tags:
  - meta
  - codebase-graph
related: []
sources:
  - "library/knowledge/private/codebase-graph/meta/source-receipt.json"
  - "library/knowledge/private/codebase-graph/graph.json"
---

# Local graph extraction receipt

## Scope and authority

The caller relayed explicit approval to generate a local-only graph and wiki for `src/sec_redteam`, with repository writes restricted to `library/knowledge/private/codebase-graph/`. This domain did not exist before this run. Direct invocation; `partial_scan: true`. No driver queue, global index or reconciliation was requested or run.

Source HEAD is `1e71d28b23881f5d1c76849003cd144cfe545947`. All 21 scoped source files matched that commit byte-for-byte during verification. [source-receipt.json](source-receipt.json) records SHA-256, size and coverage per file. The only available scoped commit was the single-line publication baseline; no qualifying ADR signal or prior wiki contract was found. No ADR, contradiction artifact or invented historical decision was filed.

## Tool and safety evidence

Installed extractor: `@deeplake/hivemind` 0.7.161, using tree-sitter Python. The installed package metadata was read before execution. No package installation, source checkout substitution or agent handoff occurred.

The following installed bundle locations were inspected, not assumed from a proposed command:

- `@deeplake/hivemind/bundle/graph-P7USWKOW.js:197-200`: push returns immediately when `HIVEMIND_GRAPH_PUSH=0`.
- `@deeplake/hivemind/bundle/graph-P7USWKOW.js:3009-3025`: build scope comes from `--cwd`, then source discovery.
- `@deeplake/hivemind/bundle/graph-P7USWKOW.js:3055-3117`: snapshot metadata, push and optional auto-doc refresh paths.
- `@deeplake/hivemind/bundle/chunk-U5AF2ZBC.js:437-441`: graph state is HOME-relative absent an explicit graphs-home override.
- `@deeplake/hivemind/bundle/chunk-U5AF2ZBC.js:514-537`: snapshot, latest-commit, last-build and history writes stay in the chosen state directory.
- `@deeplake/hivemind/bundle/chunk-43HMEDFQ.js:66-82`: credentials are read from HOME; no token/org yields null config.
- `@deeplake/hivemind/bundle/chunk-P6DQCJZO.js:5-18`: auto-doc registry override and empty-registry fallback.

The build used `env -i`, an isolated temporary HOME, `HIVEMIND_GRAPH_PUSH=0`, `HIVEMIND_GRAPH_PULL=0`, `HIVEMIND_DOCS_AUTO_FILE=/dev/null`, and `sandbox-exec` with `(version 1)(allow default)(deny network*)`. Its executable and PATH used the already installed Node distribution. Source discovery was restricted through `graph build --cwd` to the approved subtree.

Observed build result: exit 0; 14 files extracted; zero skipped files, parse warnings or cache hits; 58 nodes; 87 edges; `Cloud: skipped (HIVEMIND_GRAPH_PUSH=0)`. No auto-doc spawn was reported. The isolated CLI's own graph cache/snapshot bookkeeping remains temporary state, not repository or real-HOME global wiki state. No cleanup of unrelated or temporary files was attempted.

## Export transformations

The raw graph contains an absolute worktree path in its observation section, so it was **not copied verbatim** into the repository.

1. Removed the observation object, including absolute worktree path, timestamp and branch.
2. Removed the machine-derived repo key; stored source HEAD separately in the receipt.
3. Prefixed internal IDs, source files and unresolved internal paths with `src/sec_redteam/`.
4. Sorted nodes by ID, edges by source/target/relation/ordinal, and JSON object keys.
5. Preserved all 58 nodes and 87 edges, including original confidence and degree/entrypoint fields.
6. Checked for absolute home/temp paths and common credential/private-key patterns before writing the graph.

The normalized graph checksum is in [source-receipt.json](source-receipt.json). It is intentionally different from the raw extractor content checksum. Sorting makes this representation deterministic for the same extracted content; no cross-version or future-extractor reproducibility guarantee is implied.

## Wiki coverage

- 49 extracted entity pages: 14 file modules, 22 functions, ten classes/data models and three significant constants.
- Seven filename-only JSON query stubs, with `language: json`, `source_extension: .json` and `status: stub`.
- Three concept pages, one navigation README and this receipt: **61 Markdown pages** total.
- Three method nodes remain represented in their owning class pages. Six incidental constants remain in the graph without standalone prose pages.
- Five substantive authoring groups contain 9, 11, 10, 11 and 11 entity/concept pages; seven filename-only query stubs form a separate configuration pass. No padding pages were created to satisfy a chunk-size target.
- Python signatures and graph edges were cross-checked against source using the standard-library AST without importing or running project modules. The truncated extractor signature for `build_workflow_plan` was expanded from `src/sec_redteam/workflows/planner.py:121-126`.

## Checks actually run

Before this receipt was added, a local Python verification pass passed these checks:

- All three JSON artifacts parsed; graph canonical formatting/order and checksum matched.
- 58 unique nodes, 87 edges and endpoint integrity passed, allowing explicit external/unresolved targets.
- All 35 class/function/method declarations matched an independent Python AST enumeration and starting line numbers.
- All 21 source files matched recorded hashes, sizes and Git HEAD bytes; `git diff -- src/sec_redteam` was empty.
- All 60 then-existing Markdown pages parsed as YAML-frontmatter documents and stayed below 300 lines; the longest was 91 lines.
- 466 wikilink occurrences resolved; dependency/caller backlinks were reciprocal.
- 569 source-coordinate occurrences were within existing source-file line bounds.
- 89 Markdown links resolved, allowing only this then-pending receipt page.
- No generated file used a driver-owned filename. Exported artifacts contained no absolute home/temp paths or common token/private-key patterns. This pattern check is not a comprehensive secret-detection guarantee.
- Structured response page coverage and `partial_scan: true` were checked.

No application tests, ingestion, provider requests, scanners, exercise execution, cloud sync, native hooks, commits or pushes were run. This receipt verifies documentation artifacts, not application behavior or comprehensive security properties.

## Limits and gaps

The graph contains 36 external-import edges to 17 distinct modules and one unresolved inheritance edge to `Protocol`; their targets are not local declaration nodes. `EXTRACTED` confidence, export flags and entrypoint flags are retained extractor labels, not independently verified runtime certainty.

Receiver dispatch is incomplete: `client.search_and_contents` at `src/sec_redteam/ingest/pipeline.py:86` and SDK dispatch at `src/sec_redteam/ingest/exa_client.py:33` do not resolve to callable implementations in this snapshot. Type-reference and module-level call relationships are not exhaustively represented. Absence of an edge does not prove absence of a dependency; no missing edge was guessed into existence.

JSON contents were hashed but not semantically extracted. Tests, dependency implementations, `.env`, corpus `data/` and files outside the approved subtree are outside this scan. Existing sibling documentation and other workers' files were not part of the write domain.

[response-payload.json](response-payload.json) contains all required response keys, 65 detected entities including seven stubs, and 46 explicitly located gaps (37 boundary targets, seven JSON files and two receiver calls). No global reconciliation is authorized by the payload. Future updates must compare these contracts and use the full contradiction protocol when they change.
