import json

import yaml

from gendiff.build_diff import build_diff
from gendiff.formatters.format_stylish import format_stylish


def read_file(file):
    try:
        if file.endswith(".json"):
            return json.load(open(file))
        elif file.endswith((".yaml", ".yml")):
            return yaml.safe_load(open(file))
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
