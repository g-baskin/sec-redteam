# QA Report: bounded documentation and repository setup

**Specification:** caller-supplied acceptance brief in this review invocation: current app docs, Library, local wiki/code graph, and missing Get Started files; automation inactive for billing. This is the supplied short specification, not an inferred feature PRD. No PRD/IRD was commissioned (`library/README.md:45`). Conversation-spec digest: unavailable; no invented approval or plan identity.
**Audit date:** 2026-10-19 local; verification finished 2026-10-20 UTC.
**Base / HEAD:** `main`, `1e71d28b23881f5d1c76849003cd144cfe545947` for both; reviewed dirty working tree, not a new commit.
**Auditor:** quality-wasp-drone.
**Report destination:** `docs/setup-quality-review.md`, explicitly assigned by caller; only this report authored. No implementation changes.
**Candidate:** 105 files, 337,588 bytes; SHA-256 of the sorted exact-byte manifest below: `67b07ad844c94a203da2591f53c6f4fa692d3a581ac357760b3bf92c9020e668`. Scope: README, EditorConfig, example environment file, `.github/**`, contribution/security/changelog docs, Get Started, and Library excluding notes. No symlinks observed. File contents/path identity only; modes are not included. No scoped deletions observed.
**Supporting setup record:** `docs/get-started.md`, SHA-256 `5f726673040f35ee97ef8f44e76618c28f0298f714de8981f971fb5afc988e73` (implementation account, not independent approval).
**Security prerequisite:** `docs/setup-security-review.md`, SHA-256 `349657f8648b61db0ab7be0b3b17bb7aaf89be94d1dc8e3a7c9c172efff72713`; final comparison recorded at `2026-10-20T02:42:55Z`. Its candidate fingerprint matches this review before and after checks; zero scoped findings. No ordering violation or stale Security input detected.
**Verification packet:** embedded below to honor single-file ownership. Hashes establish byte identity, not signed provenance, security certification or permission to publish.

### Verification receipts and coverage boundary

All commands ran locally from the repository root. No application modules were imported by the static scripts.

| Check | Actual observation / result | Limit |
| --- | --- | --- |
| `git status --short`, `git diff --stat`, `git diff 1e71d28b23881f5d1c76849003cd144cfe545947...HEAD --stat`, `git diff --cached --stat`, `git diff -- README.md` | PASS: committed/staged deltas empty; README modified; other scoped files untracked. Read the README diff and scoped new documentation. | Pre-existing unrelated untracked artifacts preserved, not attributed to this run. |
| `git diff --check` | PASS, exit 0. | Tracked diff only; not an untracked-file lint result. |
| `git diff --exit-code HEAD -- src tests pyproject.toml .gitignore LICENSE` | PASS, exit 0; no tracked changes. | Not a full repository integrity/security audit. |
| `python3 -B -u -` standard-library static verification here-document | PASS, exit 0, Python 3.12.1; start `2026-10-20T02:48:17.946513Z`, end `2026-10-20T02:48:18.753589Z`. Independently matched all 35 class/function/method declarations and starting lines to AST, all 14 module nodes, and named-call evidence for 31 call edges. Verified 58 unique nodes, 87 edges, 37 boundary targets, 21 source hashes/sizes/HEAD bytes, graph checksum and partial/no-reconciliation flags. | Direct-call evidence is static, not receiver-dispatch or complete dependency resolution. Terminal results observed; no separate log file authored. |
| Same static verification | PASS: all 61 wiki Markdown pages below 300 lines; response page list exact; 466 wikilinks resolve; 573 source-coordinate occurrences in bounds; 47 dependency pairs reciprocal. Independently confirmed 206 relative Markdown links across 97 scoped Markdown files, inactive workflow/Dependabot filenames, absent completion marker, and unchanged 105-file fingerprint. | Frontmatter delimiters checked here; YAML parsing is imported evidence below. Citation bounds and link resolution alone do not prove prose semantics; significant claims were also source-read. |
| Earlier `python3 -B -` AST/hash attempt | INCOMPLETE: tool timed out at 1,000 ms, no usable result. Repeated with 10,000 ms allowance successfully, then included in the complete verification above. | Not silently counted as passing. No application test was involved. |
| Significant behavioral claims | PASS, source qualification: fixed plans/nonexecution, evidence ordering/fallback, soft post-fetch budget, first-writer-wins storage, commit-before-export, allowlist replacement, truthy numeric overrides, preset/path/CLI contracts; detailed evidence below. | No new runtime behavior exercised. |
| Existing tests | Imported caller PASS: 18/18 under OS network denial, plugins/cache/bytecode disabled; not rerun. `docs/get-started.md:39`. | Exact raw runner log, timestamps and digest not provided in this handoff. Earlier domain-author 10/18-test accounts describe separate checks, not this review's execution. |
| YAML and security scanning | Imported PASS: inactive templates parse; Security reports Gitleaks 8.30.1 exit 0, 105 outputs clean. `docs/get-started.md:40`; `docs/setup-security-review.md:21-23`. | Not independently replayed; no install, network, scan upload or comprehensive application-security claim. |
| Remote settings and action provenance | Imported caller observation: owner-approved PVR enabled, other settings unchanged, zero hosted workflows; action SHAs verified by author. `docs/get-started.md:25-29,41,46-50`. | No GitHub API calls here; historical observation, not a fresh remote-state attestation. |
| Fresh install, hosted CI, Mermaid rendering, live Exa, native integration, cloud graph refresh | NOT_RUN / excluded by scope. | No implied approval or coverage. |

The wiki author's final whole-domain pass was incomplete at handoff. The caller's later whole-domain verification was supplied, and this review independently repeated the structural/source-identity checks above. The historical extraction receipt's 60-page/569-citation counts remain explicitly pre-receipt observations (`library/knowledge/private/codebase-graph/meta/extraction-receipt.md:66-75`), not a defect in the current 61-page result.

Generated-output identity: `graph.json` SHA-256 `c7a029bc9a93666d7c35f54365b8698bdb8866357c0352dd2b4ee67045bf705d`. Recorded producer: Hivemind 0.7.161/tree-sitter, isolated local build plus normalization, described in `library/knowledge/private/codebase-graph/meta/extraction-receipt.md:24-53`. Producer isolation/execution history is imported receipt evidence, not independently replayed. Retained limitations: seven filename-only JSON stubs, three methods documented with their classes, six incidental constants without standalone pages, 36 external import targets and one unresolved Protocol inheritance target; no global reconciliation.

## Summary

**PASS for the bounded docs/setup specification: Critical 0, Warning 0, Suggestion 0.** Significant behavioral claims match unchanged source, graph declaration coverage is complete for its declared Python subtree, and current structural checks pass against the Security-reviewed bytes. This does not declare full onboarding complete: billing-related automation, human-only notes and the completion marker remain deliberately deferred; commit/push/merge/publication require separate approval.

## Scorecard

| Category | Status | Notes |
| --- | --- | --- |
| Completeness | ✅ | Requested app references, Library, bounded wiki/graph and setup files present; agreed deferrals explicit. |
| Correctness | ✅ | Significant semantics independently traced to source; declaration, hash and link checks pass. |
| Alignment | ✅ | Python baseline, local-only partial scan, billing pause and assigned report ownership respected. |
| Gaps | ✅ | No unacknowledged gap found within the supplied brief; runtime/provider/rendering limits retained. |
| Detrimental | ✅ | No source/dependency/test changes, active automation, fabricated completion marker or publication claim. |

## Critical Issues (must fix)

None.

## Warnings (should fix)

None. Existing application caveats are accurately documented, not newly introduced defects to fix in this task.

## Suggestions (consider improving)

None within this bounded review. No generic tooling or unrelated application-audit expansion proposed.

## Plan Item Traceability

The IDs below label the caller's supplied requirements/non-goals, not invented PRD acceptance criteria. “Pass” is limited to the stated evidence; imported historical observations are identified separately.

| ID | Requirement / claim | Status | Implementation and independent evidence |
| --- | --- | --- | --- |
| R1 | Explain current app, not planned web/scanner features | Pass | `README.md:3-29`; `library/knowledge/private/architecture/system-overview.md:25-107`; source `src/sec_redteam/workflows/planner.py:6-172`. Fixed phase lists and printed assumptions do not execute exercises. |
| R2 | Usable offline quickstart and CLI reference | Pass (static; smoke evidence imported) | `README.md:7-19,31-70`; `library/knowledge/public/usage/cli-guide.md:20-178`; source `src/sec_redteam/workflows/cli.py:13-38`, `workflows/evidence.py:19-21` under the same package. Missing database returns before connecting; workflow imports use standard library/local workflow modules. All explicit parser flags and eight preset values compared to source. |
| R3 | Accurate evidence semantics | Pass | `library/knowledge/public/usage/cli-guide.md:72-84`; `src/sec_redteam/workflows/evidence.py:10-61`: `ORDER BY rowid DESC`, keyword OR/LIKE, excerpt prefix, missing-path return, finally-close; `src/sec_redteam/workflows/planner.py:127-171`: normalization and separate evidence attachment. |
| R4 | Accurate ingestion/storage/failure boundaries | Pass | `library/knowledge/private/data/corpus-storage.md:23-161`; `src/sec_redteam/ingest/storage.py:28-75`: complete DDL, bound INSERT and `conn.commit()`; `src/sec_redteam/ingest/pipeline.py:100-160`: post-fetch estimate, seen-before-length, commit-before-chunks/export. No refresh/replay guarantee invented. |
| R5 | Accurate operator caveats and paths | Pass | `library/knowledge/private/operations/runbook.md:35-73,100-149`; `src/sec_redteam/ingest/cli.py:72-85`: replacement allowlist and `value or preset`; `src/sec_redteam/ingest/utils.py:10-41`: registrable domain and character chunks; `src/sec_redteam/ingest/pipeline.py:96-98,166-181`: failed searches bypass delay, final count returned. Logging extras absent from configured formatter confirmed at `src/sec_redteam/ingest/cli.py:65-68`. |
| R6 | Library schema/navigation without speculative plans | Pass | `library/README.md:18-45`; `library/knowledge/private/standards/documentation-framework.md:30-65,83-135`; lifecycle/navigation shelves present and links resolve. No PRDs/IRDs/ADRs/CTRs invented. |
| R7 | Local wiki and graph with declared coverage | Pass | `library/knowledge/private/codebase-graph/README.md:17-27,56-74`; receipt/payload/graph identities and independent AST/page checks above. All 35 declarations present; missing receiver/external resolution explicitly bounded, not misreported as full runtime call coverage. |
| R8 | Missing Python-appropriate repository baseline files | Pass | `.editorconfig:1-18`, `.env.example:1-4`, `.github/CODEOWNERS:1-6`, issue/PR templates, `CONTRIBUTING.md:5-38`, `SECURITY.md:5-26`, `CHANGELOG.md:5-21`; creation inventory `docs/get-started.md:19-34`. No invented response SLA, release tag, enforced branch rule or lint/type pass. |
| R9 | CI/dependency automation inactive for billing | Pass locally; remote state imported | `.github/workflows/ci.yml.disabled:1-26`, `.github/dependabot.yml.disabled:1-9`, `.github/README.md:3-13`; zero active local workflow/Dependabot YAML. Future workflow is manual-only/read-only; activation requires approval. |
| R10 | Intentional badge omission and partial setup marker | Pass | `README.md:1-86` has no badges; no verified hosted CI endpoint asserted. `docs/get-started.md:52-60` documents withheld `wasp-nest.lock`, human notes and automation deferrals; marker absent. These are accepted boundaries, not completion defects. |
| R11 | Approved PVR change, no other settings changes | Imported observation only | `SECURITY.md:9`, `docs/get-started.md:46-50`; accepted caller/Security evidence, no new API verification or settings mutation. |
| NG1 | Preserve source, tests, manifest, ignore rules and license | Pass | Empty tracked diff against the declared HEAD; all 21 scoped source files also match exact HEAD bytes. No implementation work undertaken. |
| NG2 | Security before final Quality | Pass | Matching Security fingerprint and report identity above; no unresolved scoped findings. |
| NG3 | No installs, network/upload, data/secret/notes reads, agents, Git mutation or global reconciliation | Pass for this reviewer | Static/read-only review commands only; this report is the sole authored output. No repository `.env`, corpus `data/`, `CLAUDE.md`, `.gg` state or notes read; explicitly requested installed skill guides were read. No additional agent or cross-pack handoff. |
| NG4 | Preserve other workers and leave fixes to caller | Pass | Unrelated untracked files untouched. No changes to source, configuration, existing reports or evidence; no cleanup/restoration/movement. |

Coverage ledger: spec and standards checked for setup/root policies, Library scaffold/domain docs, and wiki/graph; no actionable findings. Agent-output checks covered unsupported completion claims, invented flags/symbols, test/dependency drift and artifact identity. Runtime tests imported only, not rerun; remote/provider/rendering checks not performed. A source-citation to excluded `CLAUDE.md` in existing domain docs was not reopened or independently validated.

## Files Changed

Reviewed change inventory: README modified; 104 scoped additions currently untracked. Pre-existing `CLAUDE.md`, `.gg-checklist.json`, `docs/reviews/`, and the prerequisite Security report are not changes attributed to this deliverable. The Quality report is outside its own candidate manifest.

Each row below gives status, purpose, and exact content SHA-256. Reproduce the fingerprint by concatenating `SHA256 + "  " + path + "\n"` in path order; exclude this report and the separately pinned Security report. This is a scoped manifest, not a whole-repository identity.

| Path | Status / purpose | SHA-256 |
| --- | --- | --- |
| `.editorconfig` | A — repository baseline/setup documentation | `16b725578cc4efd980209803ceb7df16655549d90198b2c5ae8ebb179db9859f` |
| `.env.example` | A — repository baseline/setup documentation | `6b2708b90da8495f4852b00b619c2fe42c1d4758b58234661cf4d0b3827431bc` |
| `.github/CODEOWNERS` | A — governance or inactive automation template | `b8aefa3a63ec547e069b88b765945ff808f0a5a768ed671aa64d7ef380f1d8b0` |
| `.github/ISSUE_TEMPLATE/bug_report.md` | A — governance or inactive automation template | `c1858f248430b146a018b69fff643991e606704c8d4b32e348eb29471bb21603` |
| `.github/ISSUE_TEMPLATE/feature_request.md` | A — governance or inactive automation template | `6d5c74d5506ebf47a3156a83f2587e64e038d8ea751bc04263eae31ba2522657` |
| `.github/PULL_REQUEST_TEMPLATE.md` | A — governance or inactive automation template | `0b15c3cfc933e7d701e47e5d5a51d7ef3813e14b58f9696a02e66ed5801d95e4` |
| `.github/README.md` | A — navigation and scope rules | `3f17ba40202af6caaa06589d32fc69c71dfe93ede9df12b3653c6fb24e216109` |
| `.github/dependabot.yml.disabled` | A — governance or inactive automation template | `b55e1c8bd16ebc4d122c6e64c508e2cabae838ec2a3530986e5ed540905da575` |
| `.github/workflows/ci.yml.disabled` | A — governance or inactive automation template | `2d84d921999ce962f1220934b457f91da1abe4cda03de21b6267fb8541fab55d` |
| `CHANGELOG.md` | A — repository baseline/setup documentation | `1c830712675fa8adb026d787756f7166405811acfbe358330a2330a9d772532f` |
| `CONTRIBUTING.md` | A — repository baseline/setup documentation | `2e3e5923a38b23f90cc57e6facbf08681a78eeb87b5a07b10a9dd20d8a7d2a63` |
| `README.md` | M — current CLI overview and quickstart | `0b0db1ee4fdf3d3bcd674c8527726905d30e6357be8b77804c3e7ce4d7e920c5` |
| `SECURITY.md` | A — repository baseline/setup documentation | `975e2e708146130eaf2136a597e6a46870836c4efe957c3f4b4c689dd8b2243c` |
| `docs/get-started.md` | A — repository baseline/setup documentation | `5f726673040f35ee97ef8f44e76618c28f0298f714de8981f971fb5afc988e73` |
| `library/README.md` | A — navigation and scope rules | `073287b1884ac27ee6f9665b0b2891d4cf1fd8c44f947d091245dd5151c6b48c` |
| `library/issues/README.md` | A — navigation and scope rules | `da36a4df81b017747aefba53179a7191ee42e5ae38eeafb0078f81d95c56f622` |
| `library/issues/backlog/README.md` | A — navigation and scope rules | `4059ee9e5a48f96150a22e9924c63c967471dfd770da77a31cc278c49b900044` |
| `library/issues/completed/README.md` | A — navigation and scope rules | `56100413a286489df4288c54713899d56497c29b8e95e1cf01ebdeb29ce54f0b` |
| `library/issues/in-work/README.md` | A — navigation and scope rules | `5cf1f52ab49fa229e853e696d01af473aeea3179619c63dc1c47e96003c9b2b2` |
| `library/knowledge/README.md` | A — navigation and scope rules | `9fab50f16f4c0f207a3ad0738618add3b8b8b4b472a68a3772cec2afeed67aa9` |
| `library/knowledge/private/README.md` | A — navigation and scope rules | `86aa858a64e0ff0854b5590586187760ba849ce27e321d6d33c57f193158558c` |
| `library/knowledge/private/architecture/README.md` | A — navigation and scope rules | `31e6eac1068abefd31b381c38a6c1f6e66aaf5152aa1f031a044b6388951d5a5` |
| `library/knowledge/private/architecture/system-overview.md` | A — source-cited reference or standard | `1539a0ecfa814da4f845ec5dea39af7a2f67663798810544d48e5bd805c56f9f` |
| `library/knowledge/private/codebase-graph/README.md` | A — navigation and scope rules | `0da89d4f0811685e05e7d9f192045b551cdde11a66623f7f4e32a0f798e49eba` |
| `library/knowledge/private/codebase-graph/concepts/corpus-filter-and-budget.md` | A — source-grounded concept | `6c8b960ca8b3a18615e9ac1fbceb4e3a2f6c5ff22c21f3000b876b454fce3f88` |
| `library/knowledge/private/codebase-graph/concepts/evidence-is-attachment.md` | A — source-grounded concept | `9616061e3606ae4221dc1a9f85e49d58f279ae724f00890374442fd589154818` |
| `library/knowledge/private/codebase-graph/concepts/insert-before-export.md` | A — source-grounded concept | `7830628835d85f03d219b7eaf8828c2b91923121630a21ac5c4e88c9b017fba8` |
| `library/knowledge/private/codebase-graph/entities/__init__-module.md` | A — atomic entity or explicit JSON stub | `b6a8818b7d38f9db0084136e47dbfbf3c4c252fdd630372305f5044ef00711ec` |
| `library/knowledge/private/codebase-graph/entities/aggressive_breadth_queries.md` | A — atomic entity or explicit JSON stub | `128c8532d1c0c072087bf1ef9a5f2f743f4d651bad160f9bbbf7ee3e2320ba96` |
| `library/knowledge/private/codebase-graph/entities/badass_today_queries.md` | A — atomic entity or explicit JSON stub | `a19f42db20486ca1271fd4e49ed1bf459ae78e2f2494e9979f08336d93607360` |
| `library/knowledge/private/codebase-graph/entities/compliance_deep_queries.md` | A — atomic entity or explicit JSON stub | `a8f87aec4eac4f5fd3094e5ef7a1e4b66d6b7b80fcca86be8da13e14fa92d29d` |
| `library/knowledge/private/codebase-graph/entities/compliance_surge_queries.md` | A — atomic entity or explicit JSON stub | `e0b340e97dd1b5dc20f24f8e464500f9ddcadaf6f74715414b25dd58330a3ff4` |
| `library/knowledge/private/codebase-graph/entities/default_queries.md` | A — atomic entity or explicit JSON stub | `255046d96e0c62b7ee04efb554d93381a98d60e421090bb957ba5044f71a4537` |
| `library/knowledge/private/codebase-graph/entities/ingest-__init__-module.md` | A — atomic entity or explicit JSON stub | `563474ae9f894f6984ab5938807a22e093d67cfbf44cc99bbf5e1646ff4eaa13` |
| `library/knowledge/private/codebase-graph/entities/ingest-cli-DEFAULT-ALLOWED-DOMAINS.md` | A — atomic entity or explicit JSON stub | `2af948ba6f2e055a574c5df9aa4c124fe9adf7e52eac1d2f7a51ea7c40dd0b72` |
| `library/knowledge/private/codebase-graph/entities/ingest-cli-build-parser.md` | A — atomic entity or explicit JSON stub | `a59bac9d3d91bbd2d24d77386bef85efbf57a4a3044877425ce8afdda9545812` |
| `library/knowledge/private/codebase-graph/entities/ingest-cli-main.md` | A — atomic entity or explicit JSON stub | `b8ca136c3a32d10e40f5647ec6a4353d85110d2081b0a13444511046b4fe415c` |
| `library/knowledge/private/codebase-graph/entities/ingest-cli-module.md` | A — atomic entity or explicit JSON stub | `5d319ad8d9e7fbbb4aa677b9389435754e45072c9fd0c53356d049634e70982f` |
| `library/knowledge/private/codebase-graph/entities/ingest-exa_client-ExaSearchClient.md` | A — atomic entity or explicit JSON stub | `627375a7316ec843285accd9f080ae1fc6ea4d4ca3580806902d46d98ca98a69` |
| `library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchClient.md` | A — atomic entity or explicit JSON stub | `663419bda9f0c8ca695b520c743834f29859e266980a715b84799fcb7177f448` |
| `library/knowledge/private/codebase-graph/entities/ingest-exa_client-SearchResultItem.md` | A — atomic entity or explicit JSON stub | `7dc561e084d69e050d5ef9baff24108d514931e6676db76ed2f4bf47022a97b8` |
| `library/knowledge/private/codebase-graph/entities/ingest-exa_client-module.md` | A — atomic entity or explicit JSON stub | `a40dc5b66baa7459625b3f89ef338d9f41344a07e4794146318dc15c39bbac12` |
| `library/knowledge/private/codebase-graph/entities/ingest-pipeline-ChunkedDocument.md` | A — atomic entity or explicit JSON stub | `986cd732875c32bf4f56bae280cf1625ac2489a6eb75a8e1e85f22cba30bba7d` |
| `library/knowledge/private/codebase-graph/entities/ingest-pipeline-domain-allowed.md` | A — atomic entity or explicit JSON stub | `7d32db0f6e0e4d69464b2cdea64dbc0f2fecb26e4bebb6bede05c0e8cbad7eec` |
| `library/knowledge/private/codebase-graph/entities/ingest-pipeline-extract-best-text.md` | A — atomic entity or explicit JSON stub | `906fe480e161e8c5ffae00c5afdf04a414b70425134905338aa3fffe8ee1901e` |
| `library/knowledge/private/codebase-graph/entities/ingest-pipeline-load-queries.md` | A — atomic entity or explicit JSON stub | `bf24653518251d348096cdda787c0d1a25be66c4d0158d319b3cbe425c613034` |
| `library/knowledge/private/codebase-graph/entities/ingest-pipeline-looks-like-html.md` | A — atomic entity or explicit JSON stub | `b158cac4e26f51ff682f4c9e096c0ea9a4558fca1587d72015f19a309d8f8897` |
| `library/knowledge/private/codebase-graph/entities/ingest-pipeline-module.md` | A — atomic entity or explicit JSON stub | `6c6ce7f357dd9ff20a5e4bcfa8c503d1f285febe9c3420ea2c81865ec98d2125` |
| `library/knowledge/private/codebase-graph/entities/ingest-pipeline-run-ingestion.md` | A — atomic entity or explicit JSON stub | `485582a0bc786b0d91c64ecf27a2752e87ff35175b5a96c828d769aedb93ae81` |
| `library/knowledge/private/codebase-graph/entities/ingest-presets-IngestPreset.md` | A — atomic entity or explicit JSON stub | `98df4bf06fd7069061ebe6f7b04c11221acf8e4c2d9263fca031d97a5869a085` |
| `library/knowledge/private/codebase-graph/entities/ingest-presets-PRESETS.md` | A — atomic entity or explicit JSON stub | `a3deddcb70bf4a6edc1d54c95e7dc460399781c1ea71c25f9f1e780e01ef0020` |
| `library/knowledge/private/codebase-graph/entities/ingest-presets-module.md` | A — atomic entity or explicit JSON stub | `8dd0430316f3985efafd18ccf549f3be65e638f14181ca8b2a8ecee144da3ffc` |
| `library/knowledge/private/codebase-graph/entities/ingest-storage-DocumentRecord.md` | A — atomic entity or explicit JSON stub | `3ed565340a848fdc5342e3d4d1339c2cf671f2c5f01fd53c4f76520558ea3c07` |
| `library/knowledge/private/codebase-graph/entities/ingest-storage-init-db.md` | A — atomic entity or explicit JSON stub | `8251b1c831b0730da848bd79aa77d6de43dea7c2331fc7f00d21393f1a9615d0` |
| `library/knowledge/private/codebase-graph/entities/ingest-storage-insert-doc.md` | A — atomic entity or explicit JSON stub | `f684aaea4f4cb22031fdfa823d88c3354f3f1ca4b6a72b8bfd38cc49abe48f78` |
| `library/knowledge/private/codebase-graph/entities/ingest-storage-module.md` | A — atomic entity or explicit JSON stub | `ffbce9f5a9d79f1e95d641092a1c49d7a50a991373993f0eebd7f103e0bbd407` |
| `library/knowledge/private/codebase-graph/entities/ingest-types-IngestionSettings.md` | A — atomic entity or explicit JSON stub | `8c1037f8a83a06b35f34443c73504cff20efc61eaa2e26d7498c0c6d96f95b78` |
| `library/knowledge/private/codebase-graph/entities/ingest-types-module.md` | A — atomic entity or explicit JSON stub | `9cee65d979eba6a9b3bcfb8c90fc195ab152c05ac7406171a92d678d142a559d` |
| `library/knowledge/private/codebase-graph/entities/ingest-utils-chunk-text.md` | A — atomic entity or explicit JSON stub | `92da7951d1f46b210228c82d1e4d310f8a37db08243855e7cb1678b6a8224597` |
| `library/knowledge/private/codebase-graph/entities/ingest-utils-domain-of.md` | A — atomic entity or explicit JSON stub | `e4390d8a3a0848ae4e7d261934e49a5fc95caa655afa1655bf69cf96b6e92141` |
| `library/knowledge/private/codebase-graph/entities/ingest-utils-module.md` | A — atomic entity or explicit JSON stub | `a73a6654673ce54cb84cb7ca67652827374af87f94fb0c63f57bb5120048e94a` |
| `library/knowledge/private/codebase-graph/entities/ingest-utils-normalize-text.md` | A — atomic entity or explicit JSON stub | `20a7c96c151e96da5ee69520a495d8549fbf6c53e0a86ccea12d35c53457f96e` |
| `library/knowledge/private/codebase-graph/entities/ingest-utils-sha256-text.md` | A — atomic entity or explicit JSON stub | `e561bfcdaa7593ef1b61a9ccac1e14b57bf1ec847f0170e1a67c1f3c54446004` |
| `library/knowledge/private/codebase-graph/entities/ingest-utils-sort-deterministic.md` | A — atomic entity or explicit JSON stub | `75e9cb86540ace51126c13e8089f1798c3c92bcfac816396bf7805df04939522` |
| `library/knowledge/private/codebase-graph/entities/offsec_research_queries.md` | A — atomic entity or explicit JSON stub | `d108c2489775c1de00982de9faa73bef33ef74ce5b8248eee9697f17486a0045` |
| `library/knowledge/private/codebase-graph/entities/playbook_surge_queries.md` | A — atomic entity or explicit JSON stub | `c3145265fcebd46b4490e9b5d2cebb7f794656ea713293c2135beb02ba91cf6e` |
| `library/knowledge/private/codebase-graph/entities/workflows-__init__-module.md` | A — atomic entity or explicit JSON stub | `c979f3b41f371e61357782df7f1d1d856c501ea6c9b42f7f36272fb539df4953` |
| `library/knowledge/private/codebase-graph/entities/workflows-cli-build-parser.md` | A — atomic entity or explicit JSON stub | `92dbdecc0d64026234bb6ff635b0289140e63398fe8cd9a20e17b0ef40f2f328` |
| `library/knowledge/private/codebase-graph/entities/workflows-cli-main.md` | A — atomic entity or explicit JSON stub | `778bdaae01ad59b7a50da6897a8618ed05b3f5e34818be462905201436636585` |
| `library/knowledge/private/codebase-graph/entities/workflows-cli-module.md` | A — atomic entity or explicit JSON stub | `bf21dc33ad6bc2bb46ddafd405d66993fe536d48d9f0839f441a918a27fb7794` |
| `library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources.md` | A — atomic entity or explicit JSON stub | `12c5975f7d92f06c36d742dbbead827f6cca822d61e51f4ab254dbf120eeb2bd` |
| `library/knowledge/private/codebase-graph/entities/workflows-evidence-keywords-from-scenario.md` | A — atomic entity or explicit JSON stub | `e29776091a1e84977c71a5707537fbdb63d6b2ff2fc34cfc34f51c3ca7cc91ad` |
| `library/knowledge/private/codebase-graph/entities/workflows-evidence-module.md` | A — atomic entity or explicit JSON stub | `ad88b51d2be60f6c87f5336d46489d27cd50105c15a5ff3cfe4c4a5f5e65f840` |
| `library/knowledge/private/codebase-graph/entities/workflows-models-EvidenceSource.md` | A — atomic entity or explicit JSON stub | `af4a1f1092075d2ede5b8576f028975eb8fc292f6ac2a9bd4e3334082da6a7f3` |
| `library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPhase.md` | A — atomic entity or explicit JSON stub | `443da4738414c2c9e42829c2859c71067b0c98c0a064787a0af876ed792f29eb` |
| `library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPlan.md` | A — atomic entity or explicit JSON stub | `919dba10cd0f9bee623af462779220c6ae2ef99b4c309c85329029ce5f1252f2` |
| `library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowType.md` | A — atomic entity or explicit JSON stub | `658bd0fb87d816169d554c07ef76e04e4594dad1436c6689d54efe28586293bd` |
| `library/knowledge/private/codebase-graph/entities/workflows-models-module.md` | A — atomic entity or explicit JSON stub | `0ce3953e4bfd15eb3ac8286ef1ffb7853e8154f3a3bf1835839ea45c06854ea1` |
| `library/knowledge/private/codebase-graph/entities/workflows-planner-blue-phases.md` | A — atomic entity or explicit JSON stub | `d847b6b68b90589dfccb4804b193842b63fa0abd3746d912cb1073eff4fcd36c` |
| `library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan.md` | A — atomic entity or explicit JSON stub | `b3d9a4f8b1da93f2b6f1ba07c4cd4dc96eb6e1be9fdeda698327426e4ff77a85` |
| `library/knowledge/private/codebase-graph/entities/workflows-planner-module.md` | A — atomic entity or explicit JSON stub | `09c23f974891c630568a4914755dfec38285103e059fc5f3ca6585b6fa01fd56` |
| `library/knowledge/private/codebase-graph/entities/workflows-planner-purple-phases.md` | A — atomic entity or explicit JSON stub | `1158b7dde7465602e0a43e620be3a98804e31db6165e7369903d5d6e05fbf492` |
| `library/knowledge/private/codebase-graph/entities/workflows-planner-red-phases.md` | A — atomic entity or explicit JSON stub | `24dd7b858fc6a1844c2e90a979059a999f67ff2eed2f8b9ad0e9d1f4c79c8827` |
| `library/knowledge/private/codebase-graph/graph.json` | A — graph or provenance artifact | `c7a029bc9a93666d7c35f54365b8698bdb8866357c0352dd2b4ee67045bf705d` |
| `library/knowledge/private/codebase-graph/meta/extraction-receipt.md` | A — graph or provenance artifact | `26ae618e606b516e4afc1e8c01662cadaeb80c74b923e5795377171f1381dcb4` |
| `library/knowledge/private/codebase-graph/meta/response-payload.json` | A — graph or provenance artifact | `ef9823ccaf277591ec8625c488fbc60823f2f706dfcf6480f7a43c4d8922dcda` |
| `library/knowledge/private/codebase-graph/meta/source-receipt.json` | A — graph or provenance artifact | `36a3c4185ad7069c5dce9f6d346d9672c490bb59606fe3f24c30a1a4894d9b15` |
| `library/knowledge/private/contracts/README.md` | A — navigation and scope rules | `bfe9b604fd3ebd80cf5a5203f5090bface23d66a5be67ad4c75d3b469f0b3c22` |
| `library/knowledge/private/data/README.md` | A — navigation and scope rules | `63db50d3e5a8976f055820063c0b74e306f47e6cd8bbb27183f712b3cb852877` |
| `library/knowledge/private/data/corpus-storage.md` | A — source-cited reference or standard | `61c9a14db3b7b1818e4f5b492479afc8b5c664e899090036980dbfcc29f5a187` |
| `library/knowledge/private/operations/README.md` | A — navigation and scope rules | `a618a05590478f33a9f775a2189f512a6758ef0345805865080362fe63ae86dc` |
| `library/knowledge/private/operations/runbook.md` | A — source-cited reference or standard | `269fc9d8bdd509d3f12aef656e01cb68ab55de0f7bdb1d7e891b7ade3450e49c` |
| `library/knowledge/private/standards/README.md` | A — navigation and scope rules | `c1b4594d2ffc91e065d52a6c7800da14eb6648de1648dad52ab3f6f19aced623` |
| `library/knowledge/private/standards/documentation-framework.md` | A — source-cited reference or standard | `a1c6bed7782392e118357d748d19e19aca783ad50d9e8116bc2dcd3af690cf4f` |
| `library/knowledge/public/README.md` | A — navigation and scope rules | `15ca52b02f022680de63a6398019726930277c78405b87ba5c64bc896ec4c4fa` |
| `library/knowledge/public/faqs/README.md` | A — navigation and scope rules | `a53878ee0867aa59a8fc5775a0bee146161422f16c17727de710024a6f455e88` |
| `library/knowledge/public/guides/README.md` | A — navigation and scope rules | `40af571eaa62038bdebaae598b5bf67c22f07a063a745c7ce5c6566880868abd` |
| `library/knowledge/public/overview/README.md` | A — navigation and scope rules | `6c5b6bc8d64a855be798f1c95b7d797c4cd9fb7df2faadcb3398bb25e4ffbb77` |
| `library/knowledge/public/usage/README.md` | A — navigation and scope rules | `5f6bfaafe0a70cc9ec01fdfce84d9648cb740d5919dac2028019dedf649fb1e2` |
| `library/knowledge/public/usage/cli-guide.md` | A — source-cited reference or standard | `4a92c4f3f475b981259d6e5ba2b023d7ab329f6c9b846a9c4cf339f0607dd55b` |
| `library/requirements/README.md` | A — navigation and scope rules | `022f9b1a9f4e68de7929cb6c47e4b1b9afd7a2e0d2bbca422aeaa585c529c6f3` |
| `library/requirements/backlog/README.md` | A — navigation and scope rules | `29d7c8004445499a6c22c80dc3a370806c2b6d2e3951a579602a701f2dd3534a` |
| `library/requirements/completed/README.md` | A — navigation and scope rules | `70e5e1ca746686ff6cb34ad7a4141595fc28fe0206a3ff550494bd4a402a4d61` |
| `library/requirements/in-work/README.md` | A — navigation and scope rules | `9f04fa7a00c623c3bb92c3998fdfb359722b667a3b2f9abe0a15c0adc1788f96` |
| `library/requirements/reports/README.md` | A — navigation and scope rules | `d2ffac6b283abc22908bfeeb65efb43b62234d17f35ed5be756ea119b57c43a0` |
