"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import docunest


def test_version_is_set() -> None:
    assert docunest.__version__ == "0.1.0"
