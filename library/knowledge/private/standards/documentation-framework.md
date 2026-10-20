---
ai_description: |
  Canonical Library Schema v2 for a repository. Use this file to decide where
  PRDs, IRDs, knowledge, ADRs, reports, and human notes belong. Lifecycle is
  represented by folder location. Never read or write library/notes/ as an AI.
human_description: |
  The rules for organizing repository planning and knowledge. Read this when
  you are unsure where a document belongs or when a PRD or IRD changes state.
---

# sec-redteam Documentation Framework

Library Schema v2 gives every important document one obvious home. Think of it like labeled shelves: product plans, bug plans, reference knowledge, and scratch notes stay separate so people and AI tools can find the right source without guessing.

Version: **2.0**
Updated: **2026-10-19**

## Repository baseline and evidence

This framework describes the Python CLI baseline at source revision `1e71d28b23881f5d1c76849003cd144cfe545947`. It is a documentation standard, not a feature implementation or QA verdict.

- [pyproject.toml](../../../../pyproject.toml):5–33 declares `sec-redteam` 0.1.0, Python 3.11+, and the ingestion/workflow console entry points.
- [Ingestion pipeline](../../../../src/sec_redteam/ingest/pipeline.py):70–181 searches, filters and persists reference text. [Storage](../../../../src/sec_redteam/ingest/storage.py):23–75 stores full documents in SQLite; chunk JSONL is written only after a new insert. These writes are not one transaction.
- [Workflow CLI](../../../../src/sec_redteam/workflows/cli.py):23–38 prints a plan; [planner](../../../../src/sec_redteam/workflows/planner.py):121–172 selects hard-coded phases. [Evidence lookup](../../../../src/sec_redteam/workflows/evidence.py):19–61 reads SQLite using keyword substrings ordered by insertion recency, not JSONL or relevance ranking. Citations do not generate or change phases. Missing databases produce no evidence.
- [Exa adapter](../../../../src/sec_redteam/ingest/exa_client.py):24–33 loads environment settings and makes external requests during live ingestion. This documentation work does not run it or inspect credentials/corpus contents.
- The repository overview at the pinned source revision (`README.md:3-7`) distinguishes the baseline from the planned React/TypeScript/Vite UI, FastAPI, PostgreSQL, Celery/RabbitMQ, isolated scanner workers and ZAP integration. The [current overview](../../../../README.md) retains that distinction. Do not describe those as implemented.

Scope and authorization strings are plan text, not enforcement. No scanner or exercise execution or LLM-based planning is supplied by the baseline.

## Ownership and navigation

- Library owns scaffold/navigation READMEs and this standard.
- Domain authors own the [CLI guide](../../public/usage/cli-guide.md), [system overview](../architecture/system-overview.md), [corpus storage](../data/corpus-storage.md), and [runbook](../operations/runbook.md); Library maintains their navigation.
- Wiki owns `knowledge/private/codebase-graph/` and graph artifacts. Its driver owns `index.md`, `_index.md`, `log.md`, `hot.md` and the manifest. Do not fabricate placeholders or hand-edit these outputs; report missing driver dependencies to the caller.
- `quality-wasp-drone` and security reviewers author QA/security findings; Library only maintains report navigation. `contract-writing-wasp-drone` owns shared contract terms and acceptance.
- Existing `docs/reviews/`, `CLAUDE.md` and `.gg-checklist.json` are preserved. No new speculative PRDs, IRDs, CTRs or ADRs are needed for initialization.

Documentation was authored with manifest-managed Wasp agents and their Stingers. This does not install native registries, hooks, or providers. Resolve specialist capabilities through the installed host's component resolver before a handoff; a source checkout is not proof that a component is installed. Local graph extraction and its limitations are recorded separately in the [wiki](../codebase-graph/README.md).

## Top-level map

```text
library/
  knowledge/
    public/
    private/
  requirements/
    backlog/
    in-work/
    completed/
    reports/
  issues/
    backlog/
    in-work/
    completed/
  notes/                      # reserved for humans; not created by this scaffold
```

| Folder | What belongs there | What does not belong there |
| --- | --- | --- |
| `knowledge/public/` | End-user guides, public overviews, and FAQs | Private architecture, security details, or product plans |
| `knowledge/private/` | Architecture, ADRs, engineering standards, and internal explanations | Active product requirements or bug-fix plans |
| `requirements/` | Product and feature work written as PRDs | Reactive bugs and incidents |
| `issues/` | Reactive work written as IRDs and tied to GitHub issue numbers | Planned features |
| `notes/` | Human-only scratch material | Anything authoritative or anything an AI agent should read |

## Knowledge documents

Most knowledge files explain what is true now. Accepted shared contract records are the exception: they record exact behavior that multiple PRDs have agreed to build against.

Use `knowledge/public/` only for material approved for external readers; folder placement alone is not publication permission. Use `knowledge/private/` for internal engineering, business, security, or architecture material. When unsure, start in `private/`.

Architecture Decision Records live at:

```text
library/knowledge/private/architecture/ADR-<number>-<kebab-slug>.md
```

An ADR records one important decision, its context, alternatives, and consequences. It does not replace a PRD.

Accepted shared interface agreements live at `library/knowledge/private/contracts/CTR-<###>-<slug>.md`. The contract-writing Drone owns their terms and revisions. PRDs pin an accepted revision under `## Contract dependencies`; a Draft contract leaves affected implementation work blocked. The record stays in place while PRD folders move.

## Product Requirements Documents

A PRD is a build blueprint and an inspection checklist for planned product work. New PRDs always begin in `requirements/backlog/`.

```text
library/requirements/backlog/prd-007-user-export/
  prd-007-user-export-index.md
  prd-007a-user-export-backend.md
  prd-007b-user-export-interface.md
  qa/
```

Rules:

1. List every `prd-*` folder across backlog, in-work and completed; assign max + 1. Use three-digit zero padding, natural width at 1000 and above. Never reuse or duplicate a number.
2. Keep the index and every sub-PRD inside one `prd-<number>-<slug>/` folder.
3. Write testable acceptance criteria. A reviewer must be able to answer pass or fail from evidence.
4. Create the PRD in `backlog/`, move the entire folder to `in-work/` when implementation begins, then move it to `completed/` only after the work ships and verification passes.
5. Treat `completed/` as read-only history. Correct a shipped requirement with a new PRD or an explicitly documented amendment process.
6. Before splitting work across independent PRDs, identify shared boundaries and pin the accepted contract revision in each affected PRD.

## Issue Requirements Documents

An IRD is a focused fix plan for a bug, incident, or other reactive issue. Its number matches the GitHub issue number.

```text
library/issues/backlog/ird-042-stale-cache/
  ird-042-stale-cache-index.md
  qa/
```

Rules:

1. Create the GitHub issue first.
2. Use that issue number in the IRD folder and index filename, zero-padded to three digits (natural width for 1000+). Check every lifecycle folder for an existing IRD first; never invent a number.
3. Keep an IRD single-scope. Do not create sub-IRDs.
4. Move the entire folder from `backlog/` to `in-work/` when the fix begins, then to `completed/` after the issue is closed and the fix is verified.

## Reports and QA evidence

Evidence tied to a PRD or IRD stays inside that document's `qa/` folder. This keeps the plan and proof together.

Routine repository-wide reports that are not tied to one PRD or IRD live in:

```text
library/requirements/reports/<YYYY-MM-DD>-<type>-report.md
```

Examples include a periodic security scan, repository-health audit, or general QA sweep.

## Human notes

`library/notes/` is a human-only scratch area. AI agents must not read it, write it, summarize it, or cite it. Notes are not authoritative. When a note becomes durable knowledge, a human moves or rewrites it into the appropriate `knowledge/` path.

## Document frontmatter

Every seeded folder README uses two descriptions:

- `ai_description` tells an AI what it may do in the folder.
- `human_description` gives a quick plain-language explanation.

Content documents may add fields such as status, version, owner, and updated date when the team's workflow requires them. Do not invent metadata that nobody maintains.

## Naming rules

- Use lowercase kebab-case for folders and ordinary knowledge files.
- Use `prd-<###>-<slug>` for PRD folders.
- Use `ird-<issue-number>-<slug>` for IRD folders.
- Use `ADR-<number>-<slug>.md` for ADRs.
- Use ISO dates (`YYYY-MM-DD`) in report filenames.
- Keep filenames stable after other documents link to them.

## Choosing the right document

| If you need to... | Create or update... |
| --- | --- |
| Plan a new feature | PRD under `requirements/backlog/` |
| Fix a tracked bug or incident | IRD under `issues/backlog/` |
| Record why an architecture choice was made | ADR under `knowledge/private/architecture/` |
| Explain how the system works now | Knowledge document |
| Capture temporary personal thoughts | Human note under `notes/` |
| Record independent proof for one plan | That PRD or IRD's `qa/` folder |
| Record a repository-wide audit | `requirements/reports/` |
| Save a PRD map, wave plan or handoff packet | `requirements/plans/` |
| Record a project-wide standard such as the Definition of Done | `knowledge/private/standards/` |

## Lifecycle gate

Folder location is the lifecycle status:

```text
backlog -> in-work -> completed
```

Do not copy a folder to the next state and leave the original behind. Move the entire folder. Do not mark work complete because code exists; move it only after its acceptance criteria are verified and required security and quality checks pass.

## Maintenance and verification

1. Keep documentation grounded in source paths; label baseline, planned behavior and unrun checks separately. Refresh the source revision and citations when behavior changes.
2. Check relative links after edits and lifecycle moves. Report assigned-but-missing narrative pages separately from unexpected broken links.
3. Keep authored wiki Markdown under `knowledge/`. A derived wiki export or vault is regenerated, never edited as source. Ask its owner to regenerate stale entity pages instead of patching them in place.
4. Preserve secrets and local corpus exclusions in [.gitignore](../../../../.gitignore). Do not read `.env`, local `data/`, or human notes for documentation. This scaffold intentionally does not create `notes/`.
5. Repository setup adds [contribution guidance](../../../../CONTRIBUTING.md), a [security policy](../../../../SECURITY.md), and a [setup report](../../../../docs/get-started.md). Keep their activation state explicit: CI remains inactive for billing reasons.
6. No application tests, live ingestion, scanner execution or wiki driver run is implied by a documentation link check. Record only checks actually performed.
7. `requirements/plans/` is optional and remains unseeded until real build-planning work requires it. New content must use v2 paths; flag legacy `knowledge-base/`, top-level `architecture/`, `requirements/features/`, `requirements/issues/` or top-level `qa/` rather than extending them.

## Reusable templates and evidence

Adapt the existing repository template to the reader's outcome. Identify the real workflow, template origin and source revision before generalizing. Keep current behavior, proposed requirements and unrun checks distinct. A commit URL identifies committed content; dirty working-copy sources also need their byte hash. Preserve project assumptions, failure ordering, accepted contract pins and approval boundaries. Assign a maintenance owner and review when the source changes. A copied checklist is not proof that the workflow ran. Keep customer records and secrets out of reusable templates.
