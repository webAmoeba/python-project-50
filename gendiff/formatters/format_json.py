import json


def format_json(diff):
    result = json.dumps(diff, indent=4)
    return result
