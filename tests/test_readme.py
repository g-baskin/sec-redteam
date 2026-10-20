from pathlib import Path


def test_github_landing_readme_is_not_shadowed() -> None:
    root = Path(__file__).resolve().parents[1]
    assert (root / "README.md").is_file()

    shadowing_readmes = sorted(
        path.name
        for path in (root / ".github").iterdir()
        if path.is_file() and path.stem.casefold() == "readme"
    )
    assert shadowing_readmes == [], (
        f"GitHub prefers .github README files over the root README: {shadowing_readmes}"
    )
