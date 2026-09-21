import sys


def main() -> None:
    """This program demonstrates how to handle
    command-line arguments using sys.argv."""
    print("=== Command Quest ===")
    sys_len = len(sys.argv)

    print("Program name:", sys.argv[0])

    if sys_len > 1:
        args = sys.argv[1:]
        i = 1
        print("Arguments received:", len(args))
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1
    else:
        print("No arguments provided!")

    print(f"Total arguments: {sys_len}\n")


if __name__ == "__main__":
    main()
