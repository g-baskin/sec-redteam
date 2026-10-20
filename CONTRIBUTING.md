# Contributing to sec-redteam

The current application is a Python corpus-ingestion and workflow-planning CLI. Read the [README](README.md), [CLI guide](library/knowledge/public/usage/cli-guide.md), and [Library](library/README.md) before changing behavior.

## Local setup

Use Python 3.11+ from the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest
```

Installation downloads dependencies. Tests use synthetic inputs; do not substitute live Exa calls or private corpus data. Offline plan generation does not need credentials. For deliberate paid ingestion only, copy `.env.example` to the ignored `.env` and configure your own key. Review the [operational caveats](library/knowledge/private/operations/runbook.md) first.

## Change workflow

Search existing issues before substantial work. Agree on the integration base rather than assuming it. New features and substantial extensions use a separate `feature/<short-description>` branch and isolated worktree; preserve the original checkout and unrelated changes. Keep revisions in that worktree until accepted or abandoned. Documentation-only work does not require this feature workflow.

Use focused commits with Conventional Commit prefixes such as `docs:`, `fix:`, or `feat:` when a commit is authorized. Commit, push, PR creation, merge, deployment, and cleanup are distinct actions requiring approval in agent-assisted work.

Before a feature merge, run applicable tests, lint/types/build and acceptance checks, then Security and final Quality review. Present exact candidate/base SHAs and the proposed operation for explicit approval. Do not invent passing lint/type/build checks: this baseline configures pytest but no dedicated lint or type-check command.

## Pull requests and local checks

Use the [PR template](.github/PULL_REQUEST_TEMPLATE.md), keep changes focused, and report the commands actually run. Add a small regression test for a bug fix and update source-cited docs when behavior changes. Run `python -m pytest` in the activated development environment and `git diff --check`.

**CI is inactive due to billing.** The `.disabled` workflow and Dependabot templates must stay inactive until separately approved. Local checks are required evidence, not a substitute for review or a claim of hosted CI coverage. See [automation notes](.github/README.md).

Code-owner review is requested through [CODEOWNERS](.github/CODEOWNERS) once published; enforcement needs a repository rule. Do not imply that a local file alone protects a branch.

## Reports, secrets, and licensing

Use the public [issue templates](.github/ISSUE_TEMPLATE/) for ordinary bugs and requests. Report vulnerabilities privately through [SECURITY.md](SECURITY.md). Never include keys, `.env` values, local databases, or private findings in public reports.

Original project code uses [AGPL-3.0-only](LICENSE). Keep third-party source attribution and license boundaries intact. Record notable changes in [CHANGELOG.md](CHANGELOG.md) under `Unreleased`; a manifest version is not evidence of a published release. Release automation, hooks and commit-message enforcement are not configured by this setup.
