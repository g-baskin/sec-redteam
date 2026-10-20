from sec_redteam.workflows.planner import build_workflow_plan


def test_red_workflow_is_default_shape() -> None:
    plan = build_workflow_plan("red", scenario="phishing to c2", scope="lab")
    assert plan.workflow_type == "red"
    assert len(plan.phases) == 4
    assert plan.phases[0].name == "Plan"
    assert plan.evidence_sources == []


def test_blue_workflow_has_detection_engineering_phase() -> None:
    plan = build_workflow_plan("blue", scenario="cloud identity abuse", scope="staging")
    phase_names = [phase.name for phase in plan.phases]
    assert "Detection Engineering" in phase_names


def test_purple_workflow_has_hardening_sprint() -> None:
    plan = build_workflow_plan("purple", scenario="lateral movement", scope="lab")
    phase_names = [phase.name for phase in plan.phases]
    assert "Hardening Sprint" in phase_names
