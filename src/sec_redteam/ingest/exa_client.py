from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Protocol

from dotenv import load_dotenv
from exa_py import Exa


@dataclass(slots=True, frozen=True)
class SearchResultItem:
    title: str
    url: str
    text: str
    published_date: str | None


class SearchClient(Protocol):
    def search_and_contents(self, query: str, num_results: int) -> list[SearchResultItem]:
        ...


class ExaSearchClient:
    def __init__(self, api_key: str | None = None) -> None:
        load_dotenv()
        key = api_key or os.getenv("EXA_API_KEY")
        if not key:
            raise ValueError("EXA_API_KEY is required")
        self._client = Exa(api_key=key)

    def search_and_contents(self, query: str, num_results: int) -> list[SearchResultItem]:
        response = self._client.search_and_contents(query, num_results=num_results, text=True)
        output: list[SearchResultItem] = []

        for result in (getattr(response, "results", None) or []):
            output.append(
                SearchResultItem(
                    title=getattr(result, "title", "") or "",
                    url=getattr(result, "url", "") or "",
                    text=getattr(result, "text", "") or "",
                    published_date=getattr(result, "published_date", None),
                )
            )

        return output
