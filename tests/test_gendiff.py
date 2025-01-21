from gendiff.generate_diff import generate_diff


def test_generate_diff_jsons():
    expected = open("tests/expected/file1.txt").read()
    assert generate_diff(
        "tests/test_data/file1.json",
        "tests/test_data/file2.json") == expected


def test_generate_diff_yml_yaml():
    expected = open("tests/expected/file1.txt").read()
    assert generate_diff(
        "tests/test_data/file1.yml",
        "tests/test_data/file2.yaml") == expected


def test_generate_nested_diff():
    expected = open("tests/expected/file2.txt").read()
    assert generate_diff(
        "tests/test_data/file3.json",
        "tests/test_data/file4.json") == expected


def test_generate_nested_yaml_diff():
    expected = open("tests/expected/file2.txt").read()
    assert generate_diff(
        "tests/test_data/file3.yaml",
        "tests/test_data/file4.json") == expected
