#!/usr/bin/env python3

def garden_operations() -> None:
    """Demonstrates different types of errors in a garden context."""
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        _ = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("\nTesting FileNotFoundError...")
    try:
        f = open("missing.txt")
        if f:
            f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: missing.txt not found")
    print("\nTesting KeyError...")
    try:
        key = "missing\\_plant"
        garden = {"flowers": 5, "trees": 3}
        garden[key]
    except KeyError:
        print(f"Caught KeyError: {key}")


def test_error_types() -> None:
    """"Runs the garden operations to demonstrate different error types."""
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nTesting multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
