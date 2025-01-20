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
