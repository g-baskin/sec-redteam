# CLI guide

> Category: Usage | Version: 1.0 | Date: October 2026 | Status: Active

Use the Python CLI to generate offline exercise plans or optionally collect a reference corpus through Exa.

**Related:**
- [Project README](../../../../README.md)
- [Library index](../../../README.md)

**Source baseline:** `1e71d28b23881f5d1c76849003cd144cfe545947` (HEAD inspected on 19 October 2026). Citations below are repository-relative `path:line` references at that revision. Documentation edits do not change the baseline implementation.

## What is implemented

- Python **3.11+**, package version **0.1.0**, with two console entry points: `sec-redteam-ingest` and `sec-redteam-workflow` (`pyproject.toml:5-26`).
- Ingestion searches Exa, extracts/normalizes text, inserts full documents into SQLite, and appends character chunks to JSONL (`src/sec_redteam/ingest/pipeline.py:70-181`).
- Planning emits fixed red/blue/purple templates as JSON, optionally attaching local corpus citations. There is no LLM generation, scanner orchestration, UI, or exercise execution in these CLI paths (`src/sec_redteam/workflows/cli.py:23-38`; `src/sec_redteam/workflows/planner.py:6-172`).
- Phase names such as “Emulate” or “Live Exercise” describe instructions for people; they do not trigger actions. `--scope` and authorization assumptions are plain output fields, not enforcement or proof of permission (`src/sec_redteam/workflows/planner.py:121-172`).

## Offline quickstart: no installation or credentials

Prerequisites: a downloaded or cloned source checkout, Python 3.11+, and a POSIX shell with `mktemp`. Open the repository root before running:

```bash
PYTHONPATH=src python3 -m sec_redteam.workflows.cli \
  --scenario "credential abuse tabletop" --scope lab \
  --db "$(mktemp -d)/unused.db"
```

The command prints JSON to stdout. Expect `workflow_type` to be `red`, `scope` to be `lab`, four phases starting with `Plan`, and an empty `evidence_sources` array. It creates an empty temporary directory, not a database. A newly allocated path prevents accidental reads of an existing corpus. The planner imports only standard-library and local workflow modules; no Exa call or key is needed (`src/sec_redteam/workflows/cli.py:1-10`; `src/sec_redteam/workflows/evidence.py:19-21`; `tests/test_workflows.py:4-9`).

For blue or purple, add `--type blue` or `--type purple`. To retain output, use shell redirection to a chosen new file (`> plan.json`); the CLI itself has no output-file flag and redirection overwrites an existing file.

## Install the console commands

From the repository root, with Python 3.11+, `venv`, and `pip` available:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
```

The `dev` extra installs pytest. Use `python -m pip install -e .` instead if tests are not needed. Installation may access package indexes; the offline source-only quickstart above avoids it. These installation instructions are based on the manifest, **not a fresh-install verification** (`pyproject.toml:1-36`).

Declared runtime dependencies are `exa-py>=1.0.8`, `trafilatura>=1.9.0`, `tldextract>=5.1.2`, and `python-dateutil>=2.9.0`. The adapter also imports `dotenv`, although `python-dotenv` is not directly declared; whether it is supplied transitively depends on dependency resolution (`pyproject.toml:12-17`; `src/sec_redteam/ingest/exa_client.py:7-8`).

## Workflow command

After installation:

```bash
sec-redteam-workflow --type blue --scenario "cloud identity abuse" \
  --scope lab --db "$(mktemp -d)/unused.db"
sec-redteam-workflow --type purple --scenario "lateral movement tabletop" \
  --scope lab --db "$(mktemp -d)/unused.db"
```

### All workflow flags

| Flag | Type / default | Behavior |
|---|---|---|
| `-h`, `--help` | Switch | Show argparse help and exit. |
| `--type` | Choice: `red` (default), `blue`, `purple` | Select fixed template. |
| `--scenario` | Required string | Scenario label used in the plan and evidence search. |
| `--scope` | String: `lab` | Output label only. |
| `--db` | Path: `data/cyber_corpus.db` | Local SQLite corpus; missing path returns no evidence. |
| `--evidence-limit` | Integer: `10` | SQL result limit; use nonnegative values. Negative values are not rejected and can remove SQLite's row limit. |

Source: `src/sec_redteam/workflows/cli.py:13-38`; `src/sec_redteam/workflows/evidence.py:19-48`.

### Output and citation behavior

The JSON fields are `workflow_type`, `scenario`, `scope`, `assumptions`, `phases`, `scorecard`, and `evidence_sources`. Each phase contains `name`, `objective`, `actions`, and `outputs`. Each source contains `title`, `url`, `domain`, `topic`, and `excerpt` (`src/sec_redteam/workflows/models.py:9-34`).

Red has four phases; blue and purple have three each. Scenario whitespace is stripped; a blank scenario becomes `adversary simulation` in the plan. Evidence is queried using the original scenario before this normalization (`src/sec_redteam/workflows/planner.py:6-172`; `src/sec_redteam/workflows/cli.py:25-37`).

Evidence search:

1. Takes the first eight unique alphanumeric tokens of at least four characters from the lowercased scenario, falling back to the workflow type when none exist.
2. Matches any token as a substring in `title`, `text`, or `topic` using SQL `LIKE`.
3. Returns matches by descending `rowid` (insertion recency), **not relevance**, with the first 280 text characters as the excerpt.

Sources: `src/sec_redteam/workflows/evidence.py:10-61`. This is neither semantic search nor an LLM retrieval pipeline. Citations do not alter phase content (`src/sec_redteam/workflows/planner.py:164-172`). Review sources and exercise instructions yourself; they are not a security assessment.

## Optional paid Exa ingestion

**Do not run ingestion just to try planning.** It makes external requests and may incur charges. Obtain an Exa key and deliberately set `EXA_API_KEY` in your shell before using the ingestion CLI. Do not put credentials in shared commands, output, or version control.

Only ingestion requires this application credential. The adapter calls `load_dotenv()` and then reads `EXA_API_KEY` (unless a key was passed directly to its Python constructor). No `.env` file is required. Missing credentials raise `ValueError("EXA_API_KEY is required")` (`src/sec_redteam/ingest/exa_client.py:24-33`).

After installation and credential setup, from the repository root:

```bash
sec-redteam-ingest --preset default \
  --config src/sec_redteam/ingest/default_queries.json \
  --db data/cyber_corpus.db --jsonl data/cyber_docs.jsonl \
  --max-results-per-query 5 --budget-usd 1.0 \
  --estimated-cost-per-result-usd 0.002
```

This is a **live, potentially paid example**, not a dry run. There is no `--dry-run` flag. Parent output directories are created, SQLite is initialized if needed, and JSONL is opened in append mode (`src/sec_redteam/ingest/cli.py:27-61`; `src/sec_redteam/ingest/pipeline.py:70-86`; `src/sec_redteam/ingest/storage.py:23-46`).

### Budget is a soft estimate

`--budget-usd` is **not a provider-side or hard spending cap**. Each completed fetch increments estimated spend by `number of returned results × --estimated-cost-per-result-usd`, before filtering or deduplication. A batch reaching or exceeding the threshold is discarded before storage, although the request has already happened. Even a zero budget does not prevent the first fetch. Actual pricing can differ; the default `0.002` is a code assumption, not a verified Exa tariff. Check provider-side controls before use (`src/sec_redteam/ingest/pipeline.py:84-118`; `src/sec_redteam/ingest/cli.py:48-54`; `tests/test_pipeline.py:75-94`).

### Use the collected corpus for citations

After a successful ingestion, point planning at the same SQLite file:

```bash
sec-redteam-workflow --type red --scenario "credential abuse" \
  --scope lab --db data/cyber_corpus.db --evidence-limit 5
```

Planning does not read JSONL. A nonexistent SQLite path silently produces `evidence_sources: []`; a present but incompatible database can raise an SQL error. Zero matching rows also gives an empty list (`src/sec_redteam/workflows/evidence.py:19-61`).

## All ingestion flags

| Flag | Type / default | Behavior |
|---|---|---|
| `-h`, `--help` | Switch | Show argparse help and exit. |
| `--preset` | Choice: `default` | One of the eight profiles below. |
| `--config` | Path: preset query file | Replace the preset's query configuration only. |
| `--db` | Path: `data/cyber_corpus.db` | SQLite full-document store. |
| `--jsonl` | Path: `data/cyber_docs.jsonl` | Append-only output for new inserts. |
| `--max-results-per-query` | Integer: preset value | Requested result count per Exa query. |
| `--sleep-between-calls` | Float seconds: preset value | Delay after a successfully processed query. |
| `--min-text-len` | Integer characters: preset value | Minimum normalized text length to store. |
| `--chunk-size` | Integer: `1400` | Character window size; must be positive. |
| `--chunk-overlap` | Integer: `200` | Character overlap; must be nonnegative and smaller than chunk size. |
| `--budget-usd` | Optional float: unset | Post-fetch estimated stopping threshold, not a hard cap. |
| `--estimated-cost-per-result-usd` | Float: `0.002` | Estimate multiplier, not provider pricing. |
| `--allow-domain` | Repeated string: defaults below | Any supplied values **replace**, rather than extend, default domains. |

Sources: `src/sec_redteam/ingest/cli.py:27-88`; `src/sec_redteam/ingest/utils.py:25-39`.

Numeric overrides for results, delay, and minimum length use `value or preset_value`: passing `0` falls back to the preset. In particular, `--sleep-between-calls 0` does **not** remove the delay. The parser accepts numeric values without general range validation; choose positive counts/lengths and valid chunk settings before starting paid work (`src/sec_redteam/ingest/cli.py:74-85`).

### Eight available presets

Query files below live under `src/sec_redteam/ingest/`. All paths are relative to the current working directory.

| Preset | Query file | Results/query | Min characters | Delay seconds |
|---|---|---:|---:|---:|
| `default` | `default_queries.json` | 50 | 1200 | 0.7 |
| `badass-today` | `badass_today_queries.json` | 20 | 900 | 0.4 |
| `offsec-research` | `offsec_research_queries.json` | 20 | 1000 | 0.5 |
| `max-coverage` | `offsec_research_queries.json` | 50 | 500 | 0.2 |
| `aggressive-breadth` | `aggressive_breadth_queries.json` | 60 | 400 | 0.15 |
| `compliance-surge` | `compliance_surge_queries.json` | 80 | 300 | 0.1 |
| `compliance-deep` | `compliance_deep_queries.json` | 100 | 200 | 0.05 |
| `playbook-surge` | `playbook_surge_queries.json` | 80 | 150 | 0.1 |

Source: `src/sec_redteam/ingest/presets.py:15-64`. Tests check results/minimum lengths for the seven nondefault profiles (`tests/test_presets.py:4-43`). Preset names are query profiles, not scanner modes or guarantees of coverage/compliance.

### Query configuration and paths

A custom JSON query file is an object mapping topic names to arrays of query strings:

```json
{
  "defensive-reference": [
    "site:owasp.org authentication guidance"
  ]
}
```

The loader coerces topic/query values to strings rather than enforcing a schema. Supply the intended shape above. Topics and queries are sorted lexically before requests (`src/sec_redteam/ingest/pipeline.py:54-61`, `src/sec_redteam/ingest/pipeline.py:80-86`; `src/sec_redteam/ingest/utils.py:44-45`).

The preset paths are **not package-relative**. Run from the source repository root, or supply an explicit `--config` path. Outside that directory, also give explicit `--db` and `--jsonl` paths, then the same `--db` to planning. Installing the console scripts alone does not fix relative query paths (`src/sec_redteam/ingest/presets.py:15-64`; `src/sec_redteam/ingest/cli.py:35-42`; `src/sec_redteam/workflows/cli.py:18`).

### Domain filtering

Default strings are `mitre.org`, `owasp.org`, `nist.gov`, `cisa.gov`, `sans.org`, `github.com`, `cloud.google.com`, `learn.microsoft.com`, and `aws.amazon.com` (`src/sec_redteam/ingest/cli.py:12-24`).

The actual match compares the URL's registrable domain with these strings; for example, `sub.github.com` becomes `github.com`. The three cloud-provider subdomain entries therefore do not match their URLs as written. Providing `--allow-domain owasp.org --allow-domain mitre.org` replaces the whole default set. This is a post-fetch corpus filter, **not exact-host isolation or authorization for exercise targets** (`src/sec_redteam/ingest/utils.py:10-13`; `src/sec_redteam/ingest/pipeline.py:64-67`, `src/sec_redteam/ingest/pipeline.py:113-118`; `src/sec_redteam/ingest/cli.py:70-72`; `tests/test_utils.py:4-5`).

## Storage and operational limitations

| Observed behavior | Consequence / precaution | Evidence |
|---|---|---|
| SQLite commits before chunk generation and JSONL writing. | A later failure can leave a DB row without JSONL; these outputs are not one transaction. Validate chunk settings before ingesting. | `src/sec_redteam/ingest/storage.py:49-75`; `src/sec_redteam/ingest/pipeline.py:141-160` |
| URL-derived primary keys and unique content hashes reject repeat inserts. | First writer wins: changed pages are not refreshed, identical text cannot gain another topic, and rerunning does not repair missing JSONL. Changing export path/chunk settings does not regenerate old records. | `src/sec_redteam/ingest/pipeline.py:124-142`; `src/sec_redteam/ingest/storage.py:28-39`, `src/sec_redteam/ingest/storage.py:49-75` |
| URLs enter the in-run seen set before minimum-length validation. | A short first result can suppress a longer later result for the same URL. | `src/sec_redteam/ingest/pipeline.py:113-122` |
| Search exceptions log and continue before the delay. | Failed searches skip throttling; even all searches failing can yield normal CLI termination. Inspect errors and outputs, not only the exit code. | `src/sec_redteam/ingest/pipeline.py:84-98`, `src/sec_redteam/ingest/pipeline.py:166-181`; `src/sec_redteam/ingest/cli.py:88` |

SQLite holds the complete normalized `text`, its hash, URL, title, topic, query, domain, timestamps, and length. Each JSONL line is a document object containing metadata and a `chunks` array, not one line per chunk, and not tokenized embeddings (`src/sec_redteam/ingest/storage.py:8-20`; `src/sec_redteam/ingest/pipeline.py:21-32`, `src/sec_redteam/ingest/pipeline.py:144-160`; `src/sec_redteam/ingest/utils.py:25-41`).

## Tests and verification boundaries

With development dependencies already installed:

```bash
python -m pytest
```

The suite includes fake-client ingestion/storage and estimated-budget checks (`tests/test_pipeline.py:19-94`), text handling checks (`tests/test_pipeline_text_extract.py:4-14`), preset defaults, domain/chunk utilities, and plan shapes. These tests are not evidence of live Exa compatibility, current provider pricing, or successful fresh installation. For this documentation update, the exact README offline quickstart and all three workflow CLI variants passed local smoke checks using absent temporary database paths. The workflow and preset test files passed (10 tests) with plugin autoload and pytest's cache provider disabled. All documented explicit flags were checked against the parsers, and local links and source citation ranges were checked. The full test suite, fresh installation, and live ingestion were not run; no credentials or existing corpus were read.

## License and source material

Original code is licensed under **AGPL-3.0-only**, preserving the project's existing license declaration; see [LICENSE](../../../../LICENSE) and the [upstream license review](../../../../docs/tool-licenses.md). The manifest points to the license file (`pyproject.toml:10`). Third-party components and collected reference text retain their own terms. The code license does not relicense collected source material, credentials, scan results, or local databases.
