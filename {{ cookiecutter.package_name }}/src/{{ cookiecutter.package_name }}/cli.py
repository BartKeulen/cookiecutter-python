import argparse


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str)

    return parser.parse_args(args)


def main(args: list[str] | None = None) -> int:
    args = parse_args(args)

    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    exit(main())
