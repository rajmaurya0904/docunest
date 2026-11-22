"""Search index builder for markdown content."""

import re


def build_index(markdown: str) -> dict[str, list[int]]:
    """Build an inverted search index mapping lowercase words to 1-based line numbers.

    Each word is mapped to a list of unique 1-based line numbers where it appears,
    ordered by line number.
    """
    index: dict[str, list[int]] = {}
    lines = markdown.splitlines()
    for line_idx, line in enumerate(lines, start=1):
        words = set(re.findall(r"\b[a-zA-Z0-9]+\b", line.lower()))
        for word in words:
            if word not in index:
                index[word] = []
            index[word].append(line_idx)
    return index
