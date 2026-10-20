from __future__ import annotations

from .models import EvidenceSource, WorkflowPhase, WorkflowPlan, WorkflowType


def _red_phases(scenario: str) -> list[WorkflowPhase]:
    return [
        WorkflowPhase(
            name="Plan",
            objective="Define ATT&CK-mapped objective and success criteria.",
            actions=[
                f"Map scenario '{scenario}' to likely ATT&CK tactics and techniques.",
                "Define entry assumptions, constraints, and legal rules-of-engagement.",
                "Set measurable success criteria (access, persistence, detection coverage).",
            ],
            outputs=["Attack path hypothesis", "ROE checklist", "Success criteria"],
        ),
        WorkflowPhase(
            name="Emulate",
            objective="Run authorized adversary simulation in isolated scope.",
            actions=[
                "Execute simulation steps in lab-only environment.",
                "Capture command timeline, host artifacts, and network traces.",
                "Tag each step with ATT&CK technique IDs.",
            ],
            outputs=["Execution timeline", "Collected artifacts", "ATT&CK-tagged step log"],
        ),
        WorkflowPhase(
            name="Validate Detection",
            objective="Measure what telemetry and detections fired or missed.",
            actions=[
                "Check SIEM/EDR hits against expected behavior.",
                "Map fired/missed detections to Sigma/KQL/Splunk rules.",
                "Document blind spots and false positives.",
            ],
            outputs=["Detection hit matrix", "Blind spot list", "False-positive notes"],
        ),
        WorkflowPhase(
            name="Recovery & Lessons",
            objective="Turn findings into concrete defensive improvements.",
            actions=[
                "Run incident response steps and record MTTD/MTTR.",
                "Create hardening + detection engineering tickets.",
                "Update runbooks with observed attacker behavior.",
            ],
            outputs=["IR performance notes", "Engineering backlog", "Updated runbook items"],
        ),
    ]


def _blue_phases(scenario: str) -> list[WorkflowPhase]:
    return [
        WorkflowPhase(
            name="Telemetry Readiness",
            objective="Ensure required logging exists before testing.",
            actions=[
                f"List required logs and data sources for '{scenario}'.",
                "Validate ingestion from endpoint, identity, cloud, and network controls.",
                "Define quality checks for missing/late telemetry.",
            ],
            outputs=["Telemetry checklist", "Data quality report"],
        ),
        WorkflowPhase(
            name="Detection Engineering",
            objective="Build and tune analytic coverage.",
            actions=[
                "Implement ATT&CK-aligned detections from trusted rulesets.",
                "Tune thresholds and suppression logic.",
                "Create test cases for expected true/false outcomes.",
            ],
            outputs=["Detection pack", "Tuning notes", "Test cases"],
        ),
        WorkflowPhase(
            name="Incident Drill",
            objective="Practice consistent triage and response execution.",
            actions=[
                "Run analyst triage workflow on simulated alerts.",
                "Execute containment and eradication procedures.",
                "Capture timeline and decision points.",
            ],
            outputs=["Triage worksheet", "Response timeline", "Decision log"],
        ),
    ]


def _purple_phases(scenario: str) -> list[WorkflowPhase]:
    return [
        WorkflowPhase(
            name="Joint Planning",
            objective="Align emulation path with defender visibility goals.",
            actions=[
                f"Define collaborative objectives for '{scenario}'.",
                "Agree on ATT&CK techniques, detection expectations, and stop conditions.",
                "Set joint scorecard metrics.",
            ],
            outputs=["Joint objectives", "Technique checklist", "Scorecard"],
        ),
        WorkflowPhase(
            name="Live Exercise",
            objective="Run simulation while defenders observe in real time.",
            actions=[
                "Execute each technique step-by-step with synchronized notes.",
                "Verify what alerts and telemetry appear per step.",
                "Pause on misses and add rapid tuning.",
            ],
            outputs=["Live step log", "Detection validation notes", "Tuning deltas"],
        ),
        WorkflowPhase(
            name="Hardening Sprint",
            objective="Convert exercise gaps into immediate improvements.",
            actions=[
                "Apply detection/content fixes.",
                "Re-test failed steps until coverage improves.",
                "Document residual risk and next sprint targets.",
            ],
            outputs=["Fix list", "Re-test report", "Residual risk register"],
        ),
    ]


def build_workflow_plan(
    workflow_type: WorkflowType,
    scenario: str,
    scope: str,
    evidence_sources: list[EvidenceSource] | None = None,
) -> WorkflowPlan:
    normalized = scenario.strip() or "adversary simulation"
    if workflow_type == "red":
        phases = _red_phases(normalized)
        assumptions = [
            "Authorized environment and explicit permission are in place.",
            "Execution occurs only within approved scope.",
            "All actions are logged for after-action review.",
        ]
        scorecard = [
            "Technique execution success rate",
            "Detection hit/miss ratio",
            "MTTD and MTTR",
            "High-severity gaps closed within SLA",
        ]
    elif workflow_type == "blue":
        phases = _blue_phases(normalized)
        assumptions = [
            "Core telemetry pipelines are operational.",
            "Alert ownership and escalation paths are defined.",
        ]
        scorecard = [
            "Coverage across critical ATT&CK techniques",
            "False-positive rate",
            "Triage time-to-decision",
        ]
    else:
        phases = _purple_phases(normalized)
        assumptions = [
            "Red and blue teams share a unified test plan.",
            "Tuning can occur during exercise windows.",
        ]
        scorecard = [
            "Detection gap closure rate per exercise",
            "Re-test pass rate",
            "Time from miss to tuned detection",
        ]

    return WorkflowPlan(
        workflow_type=workflow_type,
        scenario=normalized,
        scope=scope,
        assumptions=assumptions,
        phases=phases,
        scorecard=scorecard,
        evidence_sources=evidence_sources or [],
    )
