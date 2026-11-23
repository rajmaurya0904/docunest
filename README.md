# DocuNest

**A tool that auto-generates a searchable markdown knowledge base from code comments and commit messages, for engineering teams.**

When technical documentation lives in disconnected code comments and commit logs, developers waste hours hunting for context across repositories.
DocuNest centralizes this scattered tribal knowledge into a cohesive, searchable markdown **knowledge base**.
No more scouring git log history or guessing which source file contains the architecture decision.

## Example

Running index building in Python:

```python
from docunest.search import build_index

markdown = "# Hello World\nCheck out DocuNest."
index = build_index(markdown)
print(index)
```

Output:

```python
{'hello': [1], 'world': [1], 'check': [2], 'out': [2], 'docunest': [2]}
```

## Install

Install in editable mode from the local repository:

```bash
pip install -e .
```

## Usage

- `docunest --output <path>`: write the generated knowledge base to a file (defaults to stdout).
- `docunest --include-commits`: include commit history in the generated knowledge base.
- `docunest --config <path>`: load configuration from a YAML file.

- `pytest`: run the test suite to verify code correctness.
- Python API: import `build_index` from `docunest.search` to parse markdown into a searchable word-to-line index.

## How it works

DocuNest first extracts documentation fragments from source files and, when requested, parses recent git commit messages to include their content. The collected markdown is then rendered into a unified text representation while preserving line numbers for each fragment. Finally, an inverted index is built by normalizing each word to lowercase and mapping it to the list of line numbers where it occurs, enabling fast search across the generated knowledge base.

## Limitations

- Only extracts documentation from Python docstrings; other comment styles are ignored.
- Search is based on simple keyword matching; no fuzzy matching or phrase queries.
