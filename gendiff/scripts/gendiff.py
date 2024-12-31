import json
import argparse


def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", help="Path to the first file")
    parser.add_argument("second_file", help="Path to the second file")
    parser.add_argument(
        "-f", "--format", dest="format", default="plain",
        help="set format of output"
    )
    args = parser.parse_args()

    data1 = read_json(args.first_file)
    data2 = read_json(args.second_file)

    print("First file data:", data1)
    print("Second file data:", data2)


if __name__ == "__main__":
    main()
