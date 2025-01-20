install:
	uv sync

i:
	uv tool install .

uninstall:
	uv tool uninstall hexlet-code
	uv clean

re:
	uv tool uninstall hexlet-code
	uv clean
	uv tool install .

run:
	uv run python -m gendiff.scripts.gendiff

run-h:
	uv run python -m gendiff.scripts.gendiff -h
