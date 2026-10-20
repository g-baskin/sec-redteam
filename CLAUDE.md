<!-- gg:init:start -->
# sec-redteam

Collects cybersecurity reference text through Exa into a local corpus and emits fixed red/blue/purple exercise plans with optional citations. The CLI baseline does not execute exercises, run scanners or use an LLM to generate plans.

## Data flow

- `ingest` owns search, extraction and persistence: SQLite holds full documents; JSONL holds character chunks written only for new inserts.
- `workflows` reads SQLite, not JSONL. Evidence is keyword-substring matching ordered by insertion recency, not relevance; attached sources do not change the hard-coded phases. `--scope` and authorization assumptions are output text, not enforced execution boundaries.

## Operational traps

These describe current behavior, not guarantees to preserve if deliberately fixing it.

- SQLite and JSONL are not transactional together (`ingest/storage.py`, `pipeline.py`): the DB commits before chunk validation and output writing. A failure can leave a row without JSONL, and rerunning skips it. A new JSONL path or changed chunk settings against the same DB does not regenerate an export.
- Ingestion is first-writer-wins, not refresh/upsert: URL-derived IDs and unique content hashes prevent updating changed pages or associating identical text with multiple topics. Topics/queries run in lexical order, and URLs enter the per-run seen set before length validation; a short first result can suppress a usable later one (`ingest/pipeline.py`).
- `--allow-domain` replaces the defaults despite its additive-sounding help. Matching reduces URLs to registrable domains, not exact hosts; default cloud-provider subdomain entries therefore do not match as written (`ingest/cli.py`, `utils.py`). Do not treat this corpus filter as scanner target authorization.
- `--budget-usd` is post-fetch estimated accounting, not a hard provider spending limit. Every returned result counts before filtering/deduplication; the batch reaching or exceeding the cap is discarded before storage (`ingest/pipeline.py`).
- `--sleep-between-calls 0` falls back to the preset delay because numeric CLI overrides use truthiness. Search exceptions skip the delay entirely, and even all searches failing can end with a normal CLI exit (`ingest/cli.py`, `pipeline.py`).

## Corpus-to-plan workflow

Run the CLIs from the repository root: preset query paths and default data paths are working-directory-relative, not package-relative. Elsewhere, provide explicit ingestion `--config`, `--db` and `--jsonl` paths, then point the workflow CLI's `--db` at that same database. A missing workflow database silently produces an evidence-free plan (`ingest/presets.py`, `workflows/evidence.py`).

Live ingestion uses `EXA_API_KEY` through the adapter's `load_dotenv()` call and makes external Exa requests; plan generation only reads the local corpus. Ingest before generating a plan when corpus citations are required. `.env` and collected `data/` are intentionally excluded from the published source (`.gitignore`).
<!-- gg:init:end -->

Read CONTEXT.md before naming anything.
