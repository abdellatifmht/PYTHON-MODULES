import sys
import typing


def main() -> None:
    """Simulates a data recovery system that reads and
    displays contents from an ancient text file."""
    args = sys.argv
    len_args = len(args)
    if len_args != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        return

    filename = args[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{args[1]}'")
    try:
        file: typing.IO = open(filename, 'r')
        content = file.read()
        print("---\n")
        print(content)
        print("\n---")
        file.close()
        print(f"File '{filename}' closed.")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}\n")


if __name__ == "__main__":
    main()
