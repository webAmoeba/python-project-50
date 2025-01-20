import json

import yaml


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


def generate_diff(file1, file2):
    data1 = read_file(file1)
    data2 = read_file(file2)
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    result = ["{"]

    for key in keys:
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {data1[key]}".lower())
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {data2[key]}".lower())
        elif data1[key] != data2[key]:
            result.append(f"  - {key}: {data1[key]}".lower())
            result.append(f"  + {key}: {data2[key]}".lower())
        else:
            result.append(f"    {key}: {data1[key]}".lower())

    result.append("}")
    return "\n".join(result)
