#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    """Checks if the given temperature string is valid for plants
    and returns it as an integer."""
    try:
        try:
            temp = int(temp_str)
        except ValueError:
            raise ValueError(f"'{temp_str}' is not a valid number")
        if temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

        if temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp


def test_temperature_input() -> None:
    """Tests the check_temperature function with various
    inputs to demonstrate error handling."""
    test_cases = ["25", "abc", 100, -50]
    print("=== Garden Temperature Checker ===")
    for test in test_cases:
        print("\nTesting temperature:", test)
        check_temperature(test)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
