from __future__ import annotations

import hashlib
import re
from collections.abc import Iterable

import tldextract


def domain_of(url: str) -> str:
    extracted = tldextract.extract(url)
    parts: list[str] = [part for part in [extracted.domain, extracted.suffix] if part]
    return ".".join(parts)


def normalize_text(text: str) -> str:
    no_nulls = text.replace("\x00", " ")
    return re.sub(r"\s+", " ", no_nulls).strip()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def chunk_text(text: str, *, chunk_size: int, chunk_overlap: int) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    if chunk_overlap < 0:
        raise ValueError("chunk_overlap must be >= 0")
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be < chunk_size")

    output: list[str] = []
    step = chunk_size - chunk_overlap
    start = 0

    while start < len(text):
        output.append(text[start : start + chunk_size])
        start += step

    return output


def sort_deterministic(values: Iterable[str]) -> list[str]:
    return sorted(values)
