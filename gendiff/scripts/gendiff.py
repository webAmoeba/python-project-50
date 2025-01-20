import argparse

from gendiff.read_file import read_file


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        dest="format",
        help="set format of output",
    )
    args = parser.parse_args()
    
    file1 = read_file(args.first_file)
    file2 = read_file(args.second_file)

    print(file1, file2, sep="\n")


if __name__ == "__main__":
    main()
