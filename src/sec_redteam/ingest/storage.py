from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True, frozen=True)
class DocumentRecord:
    id: str
    topic: str
    query: str
    title: str
    url: str
    domain: str
    published_at: str | None
    fetched_at: str
    text_len: int
    text: str
    sha256: str


def init_db(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS docs (
          id TEXT PRIMARY KEY,
          topic TEXT,
          query TEXT,
          title TEXT,
          url TEXT,
          domain TEXT,
          published_at TEXT,
          fetched_at TEXT,
          text_len INTEGER,
          text TEXT,
          sha256 TEXT UNIQUE
        )
        """
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_domain ON docs(domain)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_topic ON docs(topic)")
    conn.commit()
    return conn


def insert_doc(conn: sqlite3.Connection, record: DocumentRecord) -> bool:
    try:
        conn.execute(
            """
            INSERT INTO docs (
                id, topic, query, title, url, domain,
                published_at, fetched_at, text_len, text, sha256
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record.id,
                record.topic,
                record.query,
                record.title,
                record.url,
                record.domain,
                record.published_at,
                record.fetched_at,
                record.text_len,
                record.text,
                record.sha256,
            ),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
