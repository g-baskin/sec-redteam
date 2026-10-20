# sec-redteam

An open-source security testing workbench for applications you own or are authorized to assess.

**Current baseline:** Python corpus ingestion and red/blue/purple workflow planning. The web interface and scanner orchestration are under development, not available in this baseline. Existing commands below are preserved.

Planned stack: React + TypeScript + Vite, FastAPI, PostgreSQL, Celery/RabbitMQ, and isolated Linux scanner workers. The first integration is ZAP. This project does not bundle Burp, Nmap, Kali, or password/wireless tools.

## License

Original project code is licensed under **AGPL-3.0-only**. See [LICENSE](LICENSE) and the [upstream license review](docs/tool-licenses.md). Third-party components retain their own terms. Collected source material, credentials, scan results, and local databases are not included in this repository or covered by its code license.

Use testing tools only within an explicitly approved scope. Findings are evidence to investigate, not proof that an application is secure.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Required env

Put your key in your shell before running:

```bash
export EXA_API_KEY="YOUR_REAL_EXA_KEY_HERE"
```

## Run ingestion

Fastest high-impact run for today:

```bash
sec-redteam-ingest --preset badass-today
```

Offensive-security research corpus (authorized/legal learning focus):

```bash
sec-redteam-ingest --preset offsec-research
```

Maximum immediate coverage mode:

```bash
sec-redteam-ingest --preset max-coverage
```

Budget-capped run (example: cap near $4 estimated spend):

```bash
sec-redteam-ingest --preset max-coverage --budget-usd 4.0 --estimated-cost-per-result-usd 0.002
```

Custom run:

```bash
sec-redteam-ingest \
  --preset default \
  --config src/sec_redteam/ingest/default_queries.json \
  --db data/cyber_corpus.db \
  --jsonl data/cyber_docs.jsonl \
  --max-results-per-query 40 \
  --min-text-len 1000
```

## Presets

- `default`: broader baseline crawl.
- `badass-today`: focused ATT&CK + SOC + detections + GitHub rules for immediate red-team/SOC value.
- `offsec-research`: offensive-security research sources (ATT&CK, detections, DFIR, CVE intel, cloud/identity attack paths).
- `max-coverage`: high-volume pull for broadest immediate collection (more noise, more duplicates).
- `aggressive-breadth`: expanded lane coverage including NIST, SOC2, HIPAA, PCI DSS, ISO, cloud identity, DFIR, and sector advisories.

## Workflow plans (red/blue/purple)

Red is default:

```bash
sec-redteam-workflow --scenario "phishing to credential abuse" --scope lab
```

Blue/purple examples:

```bash
sec-redteam-workflow --type blue --scenario "cloud identity abuse" --scope staging
sec-redteam-workflow --type purple --scenario "lateral movement" --scope lab
```

## Test

```bash
pytest
```
