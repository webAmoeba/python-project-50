import json

import yaml

from gendiff.build_diff import build_diff
from gendiff.formatters.format_stylish import format_stylish


def read_file(file):
    try:
        if file.endswith(".json"):
            with open(file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                return json.loads(content) if content else {}
        elif file.endswith((".yaml", ".yml")):
            with open(file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                return yaml.safe_load(content) if content else {}
        else:
            raise ValueError(
                """Unsupported file format.
*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
Supported formats: .json, .yaml, .yml""")

    except Exception as e:
        raise RuntimeError(f"Error reading file {file}: {e}")


def generate_diff(file1, file2, format_name="stylish"):
    data1 = read_file(file1)
    data2 = read_file(file2)

    diff = build_diff(data1, data2)

    if format_name == "stylish":
        stylish = format_stylish(diff)
        return stylish
    else:
        return "Unsupported format name"
