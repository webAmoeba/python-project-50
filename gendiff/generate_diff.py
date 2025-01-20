import json


def read_file(file):
    return json.load(open(file))


def generate_diff(file1, file2):
    data1 = read_file(file1)
    data2 = read_file(file2)
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    result = ["{"]

    for key in keys:
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            result.append(f"  - {key}: {data1[key]}")
            result.append(f"  + {key}: {data2[key]}")
        else:
            result.append(f"    {key}: {data1[key]}")

    result.append("}")
    return "\n".join(result)
