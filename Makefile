install:
	uv sync

build:
	uv build

i:
	uv tool install .

uninstall:
	uv tool uninstall hexlet-code
	uv clean

re: uninstall i

#_______________________________________________________________________________Run

run:
	uv run python -m gendiff.scripts.gendiff

run-h:
	uv run python -m gendiff.scripts.gendiff -h

simple:
	gendiff tests/test_data/file1.json tests/test_data/file2.json

#_______________________________________________________________________________Lint

lint:
	uv run ruff check .

fix:
	uv run ruff check --fix

#_______________________________________________________________________________Tests

test:
	uv run pytest

test-vv:
	uv run pytest -vv

coverage:
	uv run pytest --cov=gendiff

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

check: test lint
