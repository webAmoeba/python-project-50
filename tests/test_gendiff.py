from gendiff.generate_diff import generate_diff


def test_generate_diff_jsons():
    expected = open("tests/expected/file1.txt").read()
    assert generate_diff(
        "tests/test_data/file1.json",
        "tests/test_data/file2.json") == expected
