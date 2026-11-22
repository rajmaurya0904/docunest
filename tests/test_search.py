"""Tests for search index builder."""

from docunest.search import build_index


def test_build_index_basic() -> None:
    markdown = """# Title
Hello world!
This is a test.
Hello again, world.
"""
    index = build_index(markdown)
    assert index["title"] == [1]
    assert index["hello"] == [2, 4]
    assert index["world"] == [2, 4]
    assert index["this"] == [3]
    assert index["is"] == [3]
    assert index["a"] == [3]
    assert index["test"] == [3]
    assert index["again"] == [4]


def test_build_index_empty() -> None:
    assert build_index("") == {}
    assert build_index("\n\n") == {}


def test_build_index_duplicates_on_same_line() -> None:
    markdown = "word word Word."
    index = build_index(markdown)
    assert index["word"] == [1]
