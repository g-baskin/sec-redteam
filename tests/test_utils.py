from sec_redteam.ingest.utils import chunk_text, domain_of, normalize_text


def test_domain_of() -> None:
    assert domain_of("https://sub.github.com/org/repo") == "github.com"


def test_normalize_text() -> None:
    assert normalize_text("a\n\n b\t\t c") == "a b c"


def test_chunk_text_overlap() -> None:
    chunks = chunk_text("abcdefghij", chunk_size=4, chunk_overlap=1)
    assert chunks == ["abcd", "defg", "ghij", "j"]
