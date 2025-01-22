import pytest

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


def test_generate_diff_empty_files():
    assert generate_diff(
        "tests/test_data/empty.json",
        "tests/test_data/empty.json") == "{\n\n}"


def test_generate_nested_empty_json():
    expected = open("tests/expected/file3.txt").read()
    assert generate_diff(
        "tests/test_data/empty.json",
        "tests/test_data/file4.json") == expected


def test_generate_plain():
    expected = open("tests/expected/plain1.txt").read()
    assert generate_diff(
        "tests/test_data/file3.json",
        "tests/test_data/file4.json",
        "plain") == expected


def test_generate_json():
    expected = open("tests/expected/json1.txt").read()
    assert generate_diff(
        "tests/test_data/file3.json",
        "tests/test_data/file4.json",
        "json") == expected


def test_invalid_file_format():
    with pytest.raises(RuntimeError, match="Unsupported file format"):
        generate_diff("tests/test_data/file1.txt", "tests/test_data/file2.txt")


def test_file_not_found():
    with pytest.raises(RuntimeError, match="File not found"):
        generate_diff("tests/test_data/non_existent.json",
                      "tests/test_data/file2.json")


def test_invalid_json():
    with pytest.raises(RuntimeError, match="Error decoding JSON file"):
        generate_diff("tests/test_data/invalid.json",
                      "tests/test_data/file2.json")


def test_invalid_yaml():
    with pytest.raises(RuntimeError, match="Error decoding YAML file"):
        generate_diff("tests/test_data/invalid.yaml",
                      "tests/test_data/file2.yaml")
