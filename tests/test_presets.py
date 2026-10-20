from sec_redteam.ingest.presets import PRESETS


def test_badass_today_preset_exists() -> None:
    preset = PRESETS["badass-today"]
    assert preset.max_results_per_query == 20
    assert preset.min_text_len == 900


def test_offsec_research_preset_exists() -> None:
    preset = PRESETS["offsec-research"]
    assert preset.max_results_per_query == 20
    assert preset.min_text_len == 1000


def test_max_coverage_preset_exists() -> None:
    preset = PRESETS["max-coverage"]
    assert preset.max_results_per_query == 50
    assert preset.min_text_len == 500


def test_aggressive_breadth_preset_exists() -> None:
    preset = PRESETS["aggressive-breadth"]
    assert preset.max_results_per_query == 60
    assert preset.min_text_len == 400


def test_compliance_surge_preset_exists() -> None:
    preset = PRESETS["compliance-surge"]
    assert preset.max_results_per_query == 80
    assert preset.min_text_len == 300


def test_compliance_deep_preset_exists() -> None:
    preset = PRESETS["compliance-deep"]
    assert preset.max_results_per_query == 100
    assert preset.min_text_len == 200


def test_playbook_surge_preset_exists() -> None:
    preset = PRESETS["playbook-surge"]
    assert preset.max_results_per_query == 80
    assert preset.min_text_len == 150
