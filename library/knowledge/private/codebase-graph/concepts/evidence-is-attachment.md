---
type: concept
title: "Evidence is an attachment, not plan generation"
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
  - "[[library/knowledge/private/codebase-graph/entities/workflows-cli-main]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPlan]]"
  - "[[library/knowledge/private/codebase-graph/entities/workflows-models-EvidenceSource]]"
sources:
  - "src/sec_redteam/workflows/cli.py:23-38"
  - "src/sec_redteam/workflows/evidence.py:19-61"
  - "src/sec_redteam/workflows/models.py:18-23"
  - "src/sec_redteam/workflows/models.py:27-34"
  - "src/sec_redteam/workflows/planner.py:121-172"
---

# Evidence is an attachment, not plan generation

## Definition

Evidence selection and fixed phase construction are separate operations joined by the workflow CLI. `src/sec_redteam/workflows/cli.py:26-38`.

## How it works

1. Scenario keywords are deduplicated and limited to eight. `src/sec_redteam/workflows/evidence.py:10-16`.
2. SQLite substring matching reads docs ordered by descending rowid, not ranked relevance; JSONL is not read. `src/sec_redteam/workflows/evidence.py:27-48`.
3. The planner selects red/blue/otherwise-purple phase templates, then attaches evidence to WorkflowPlan. `src/sec_redteam/workflows/planner.py:128-171`.

## Why it matters

A missing database silently supplies no evidence. Sources do not customize phases; scope and authorization assumptions are output fields/text, not enforced execution boundaries. `src/sec_redteam/workflows/evidence.py:20-21`; `src/sec_redteam/workflows/planner.py:130-171`.

## Examples and connections

- [[library/knowledge/private/codebase-graph/entities/workflows-cli-main]] — `src/sec_redteam/workflows/cli.py:23-38`.
- [[library/knowledge/private/codebase-graph/entities/workflows-evidence-fetch-evidence-sources]] — `src/sec_redteam/workflows/evidence.py:19-61`.
- [[library/knowledge/private/codebase-graph/entities/workflows-planner-build-workflow-plan]] — `src/sec_redteam/workflows/planner.py:121-172`.
- [[library/knowledge/private/codebase-graph/entities/workflows-models-WorkflowPlan]] — `src/sec_redteam/workflows/models.py:27-34`.
- [[library/knowledge/private/codebase-graph/entities/workflows-models-EvidenceSource]] — `src/sec_redteam/workflows/models.py:18-23`.

## Sources

- `src/sec_redteam/workflows/cli.py:23-38`.
- `src/sec_redteam/workflows/evidence.py:19-61`.
- `src/sec_redteam/workflows/planner.py:121-172`.
- `src/sec_redteam/workflows/models.py:27-34`.
- `src/sec_redteam/workflows/models.py:18-23`.
