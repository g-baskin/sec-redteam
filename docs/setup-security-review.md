# Docs/setup security review

Date: 2026-10-19 (local). **REDUCED COVERAGE: documentation/setup only**, not an application audit or deployment clearance. Used the installed Security Stinger and its audit, secrets, supply-chain and exposure guidance; its SvelteKit-specific coverage does not establish Python application security.

## Scope and fingerprint

Reviewed 105 files (337,588 bytes): `README.md`, `.editorconfig`, fake-only `.env.example`, `.github/**`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, `docs/get-started.md`, and `library/**` excluding notes. Scanned a temporary copy containing only these outputs—not the repository/history. This report is outside that input set.

- Source HEAD: `1e71d28b23881f5d1c76849003cd144cfe545947`; branch: `main`.
- Input fingerprint: `67b07ad844c94a203da2591f53c6f4fa692d3a581ac357760b3bf92c9020e668`.
- Fingerprint recipe: SHA-256 of UTF-8 concatenated `file_sha256 + "  " + repository_relative_path + "\n"`, sorted by path, covering the scope above.
- Graph SHA-256: `c7a029bc9a93666d7c35f54365b8698bdb8866357c0352dd2b4ee67045bf705d`.
- Snapshot-to-working-tree comparison at `2026-10-20T02:42:55Z`: **zero added, removed or changed scoped files**. No race observed; later edits invalidate this fingerprint. Unseen future wiki validation changes are not certified.

## Findings and checked boundaries

**No actionable finding identified against the requested docs/setup controls:** Critical 0, High 0, Medium 0, Low 0. No fixes performed.

| Boundary | Evidence and result |
| --- | --- |
| Secrets and private machine paths | Gitleaks 8.30.1 directory scan, credential-cleared environment, full redaction, no inline allow suppression: exit 0; JSON findings `[]`. Additional token/private-key, insecure-placeholder, absolute home/temp-path and execution-sink sweeps returned zero matches. `.env.example:1-4` is explicitly invalid example configuration, not a copied credential. Pattern checks are not proof of universal secret absence. |
| Nonexecution and cost | `README.md:5,19,54-61`, `SECURITY.md:24`, and `library/knowledge/public/usage/cli-guide.md:104-106,174-178` preserve fixed plans, textual scope/authorization, post-fetch soft accounting and corpus-filter limitations. No hard-budget or enforced-target guarantee found. |
| Inactive automation and future privileges | Zero local active workflow YAML files; no active Dependabot configuration. `.github/workflows/ci.yml.disabled:1-26` retains manual-only future dispatch, `contents: read`, full action SHAs, `persist-credentials: false`, ten-minute timeout and no secret injection/deployment. `.github/README.md:5-11` requires approval and dependency review before activation. SHA provenance and hosted execution were not independently rechecked. |
| Local graph and exposure | Graph checksum matches `library/knowledge/private/codebase-graph/meta/source-receipt.json:165`; 58 nodes, 87 edges, 21 receipt entries and 61 wiki Markdown pages are present. All node source paths are repository-relative. Receipts and response retain partial-scan/no-reconciliation boundaries. `library/knowledge/private/codebase-graph/meta/extraction-receipt.md:38-53` records isolated HOME, cleared environment, OS network denial, disabled push/pull/auto-docs and removal of machine metadata. Execution isolation is caller/receipt evidence, not independently replayed. |
| Deployment/synchronization claims | `library/knowledge/private/codebase-graph/README.md:66-74`, `library/README.md:43`, and `docs/get-started.md:49,58-60` distinguish local artifacts from cloud synchronization, native setup and publication approval. No assertion of completed deployment/cloud synchronization found. |
| Reporting hygiene | `SECURITY.md:9-20` directs private, synthetic, sanitized reports; `.github/ISSUE_TEMPLATE/bug_report.md:9-17` excludes credentials, private targets and corpus data. |

## Verification limits and next step

`git diff --check` passed for the scoped tracked changes; source/tests/manifest/ignore rules/license had no tracked diff against HEAD. Untracked outputs were covered by the copied-file scan, not Git's whitespace check.

Caller evidence, **not rerun here**: 18 tests passed with OS networking denied; disabled-template YAML assertions passed; private vulnerability reporting enabled with approval and GET-confirmed; existing secret scanning/push protection unchanged; Actions permitted but zero hosted workflows; default CodeQL not configured. This review made no API calls or settings changes.

Excluded: `.env`, corpus `data/`, `CLAUDE.md`, `.gg`/agent state, human notes, pre-existing reviews, Git-history secret scanning, live provider behavior, dependency installation/audit, and application authorization/tenancy, webhooks, transport, runtime injection and telemetry. No external upload, installation, exercise execution, Git mutation, remediation or additional agent was used.

Re-evaluation after fixes: not applicable. Only this report was authored. No scoped security blocker to final Quality review; Quality and orchestrator-level repository-health review remain separate gates before explicitly authorized commit/push. No cross-pack handoff was performed.
