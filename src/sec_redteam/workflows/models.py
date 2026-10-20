from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

WorkflowType = Literal["red", "blue", "purple"]


@dataclass(slots=True, frozen=True)
class WorkflowPhase:
    name: str
    objective: str
    actions: list[str]
    outputs: list[str]


@dataclass(slots=True, frozen=True)
class EvidenceSource:
    title: str
    url: str
    domain: str
    topic: str
    excerpt: str


@dataclass(slots=True, frozen=True)
class WorkflowPlan:
    workflow_type: WorkflowType
    scenario: str
    scope: str
    assumptions: list[str]
    phases: list[WorkflowPhase]
    scorecard: list[str]
    evidence_sources: list[EvidenceSource]
