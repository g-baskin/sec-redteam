# sec-redteam

![SEC-REDTEAM — Research. Plan. Defend. A futuristic armored raven surrounded by red, blue, and purple holographic evidence displays.](assets/sec-redteam-readme.png)

Collect security reference text and produce red/blue/purple exercise plans with optional local citations.

**Current baseline:** Python 3.11+ command-line tools. No web UI, scanners, exercise execution, or LLM-generated plans.

## Quickstart: offline planning

With Python 3.11+ and a downloaded or cloned checkout, open a POSIX shell in the repository root. This source-only example needs no package installation, API key, network access, or existing corpus:

```bash
PYTHONPATH=src python3 -m sec_redteam.workflows.cli \
  --scenario "credential abuse tabletop" --scope lab \
  --db "$(mktemp -d)/unused.db"
```

Expected: JSON on stdout with `workflow_type: "red"`, four phases beginning with `Plan`, and `evidence_sources: []`. The fresh temporary directory keeps this example separate from any existing corpus; no database is created.

Plans contain fixed instructions for human review, not executed actions. `--scope` and authorization assumptions are output text, **not enforced boundaries**. Only conduct exercises with explicit permission.

## Features

- Red, blue, and purple planning templates with actions, outputs, and scorecards.
- JSON plan output for review or shell redirection.
- Optional citations from a local SQLite corpus.
- Optional Exa search and text collection into SQLite.
- Character-chunk JSONL output for newly inserted documents.

**Future direction, not implemented:** React/TypeScript/Vite UI, FastAPI, PostgreSQL, Celery/RabbitMQ, isolated scanner workers, and a first ZAP integration. None is available in this baseline.

## Install

For installed command names, use Python 3.11+ with `venv` and `pip`, from the repository root (POSIX shell):

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
```

Installation may download dependencies; it is not part of the offline quickstart and was not freshly tested for this documentation update. The `dev` extra adds pytest; omit it for runtime-only installation.

## Usage

After installation, generate another plan without accessing an existing corpus:

```bash
sec-redteam-workflow --type blue --scenario "cloud identity abuse" \
  --scope lab --db "$(mktemp -d)/unused.db"
```

Use `--type purple` for the joint-team template. For citations, ingest first and pass that SQLite file with `--db`; plans never read JSONL. A missing database silently gives an evidence-free plan.

**Optional paid ingestion:** deliberately configure `EXA_API_KEY` before using the following command. It sends queries to Exa and writes local corpus files; planning does not require this key.

```bash
sec-redteam-ingest --preset default --budget-usd 1.0 \
  --estimated-cost-per-result-usd 0.002
```

**The budget is a soft estimate, not a provider spending limit.** Accounting happens after fetching; the batch reaching the threshold is discarded before storage. Actual charges can differ. Review provider-side controls before running.

## Configuration and documentation

Run from the repository root: preset query files and default `data/` paths are relative to the working directory. Elsewhere, supply explicit ingestion `--config`, `--db`, and `--jsonl` paths, then use the same `--db` for planning.

- [CLI guide](library/knowledge/public/usage/cli-guide.md): all flags, eight presets, configuration, output formats, and source-cited limitations.
- [Library index](library/README.md): documentation navigation.

`--allow-domain` replaces defaults and matches registrable domains, not exact hosts. SQLite and JSONL writes are not atomic together; rerunning does not repair missing exports. Read the guide before collecting a large corpus.

## Contributing

Keep changes grounded in current CLI behavior and update the guide when flags change. With development dependencies installed, run:

```bash
python -m pytest
```

Do not commit API keys or collected corpus files. See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and [CHANGELOG.md](CHANGELOG.md).

**CI remains inactive due to billing.** Starter automation files retain a `.disabled` suffix; use local checks until activation is explicitly approved. See the [setup report](docs/get-started.md).

## Artwork

- [README banner](assets/sec-redteam-readme.png)
- [Square skill image](assets/sec-redteam-skill.png)

## License

Original project code is licensed under the [AGPL-3.0-only](LICENSE) License. See the [upstream license review](docs/tool-licenses.md). Third-party components retain their own terms; collected source material, credentials, scan results, and local databases are not included in the published source or covered by its code license.
