import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(f"First file: {args.first_file}")
    print(f"Second file: {args.second_file}")


if __name__ == "__main__":
    main()
