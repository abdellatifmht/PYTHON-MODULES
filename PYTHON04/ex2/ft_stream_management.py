import sys
import typing


def main() -> None:
    """Cyber Archives Recovery & Preservation - File Transformation Script
    This script reads a specified text file, transforms its content by
    replacing newline characters with a custom marker, and optionally saves the
    transformed content to a new file. It demonstrates basic file handling,
    string manipulation, and user interaction in Python.
    """
    args = sys.argv
    len_args = len(args)
    if len_args != 2:
        print("Usage: ft_stream_management.py <file>\n")
        return

    filename = args[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{args[1]}'")
    try:
        file: typing.IO = open(filename, 'r')
        content = file.read()

        print("---\n")
        print(content)
        print("\n---")

        file.close()
        print(f"File '{filename}' closed.")
        print("\nTransform data:")

        print("---\n")
        transformed_content = content.replace("\n", "#\n")
        if not transformed_content.endswith("#\n"):
            transformed_content += "#"
        print(transformed_content)
        print("\n---")

        try:
            print("Enter new file name (or empty): ", end='')
            sys.stdout.flush()
            new_filename = sys.stdin.readline().strip()
            if new_filename:
                print(f"Saving data to '{new_filename}'")
                file = open(new_filename, 'w')
                file.write(transformed_content)
                print(f"Data saved to '{new_filename}'.")
            else:
                print("Not saving data.")
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled. Not saving data.", file=sys.stderr)
    except OSError as e:
        print(f"[STDERR] Error opening file"
              f" '{filename}': {e}", file=sys.stderr)
        print("Data not saved.")


if __name__ == "__main__":
    main()
