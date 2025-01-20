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

run:
	uv run python -m gendiff.scripts.gendiff

run-h:
	uv run python -m gendiff.scripts.gendiff -h

lint:
	uv run ruff check .

fix:
	uv run ruff check --fix

simple:
	gendiff tests/test_data/file1.json tests/test_data/file2.json
