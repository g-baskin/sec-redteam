from sec_redteam.ingest.pipeline import _extract_best_text, _looks_like_html


def test_looks_like_html_false_for_plain_text() -> None:
    assert _looks_like_html("this is plain text without tags") is False


def test_extract_best_text_plain_text_passthrough() -> None:
    raw = "plain text content from API"
    assert _extract_best_text(raw) == raw


def test_looks_like_html_true_for_html() -> None:
    assert _looks_like_html("<html><body><p>hello</p></body></html>") is True
