from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from .models import EvidenceSource


def _keywords_from_scenario(scenario: str) -> list[str]:
    tokens = re.findall(r"[a-zA-Z0-9]{4,}", scenario.lower())
    unique: list[str] = []
    for token in tokens:
        if token not in unique:
            unique.append(token)
    return unique[:8]


def fetch_evidence_sources(db_path: Path, scenario: str, workflow_type: str, limit: int = 10) -> list[EvidenceSource]:
    if not db_path.exists():
        return []

    keywords = _keywords_from_scenario(scenario)
    if not keywords:
        keywords = [workflow_type]

    clauses = ["(title LIKE ? OR text LIKE ? OR topic LIKE ?)"] * len(keywords)
    where = " OR ".join(clauses)

    params: list[str] = []
    for keyword in keywords:
        wildcard = f"%{keyword}%"
        params.extend([wildcard, wildcard, wildcard])

    sql = f"""
        SELECT title, url, domain, topic, substr(text, 1, 280) AS excerpt
        FROM docs
        WHERE {where}
        ORDER BY rowid DESC
        LIMIT ?
    """
    params.append(str(limit))

    conn = sqlite3.connect(db_path)
    try:
        rows = conn.execute(sql, params).fetchall()
    finally:
        conn.close()

    output: list[EvidenceSource] = []
    for title, url, domain, topic, excerpt in rows:
        output.append(
            EvidenceSource(
                title=title or "",
                url=url or "",
                domain=domain or "",
                topic=topic or "",
                excerpt=(excerpt or "").strip(),
            )
        )
    return output
