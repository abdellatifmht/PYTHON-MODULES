#!/usr/bin/env python3

def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
        ) -> None:
    """Checks the health of a plant based on its name,
    water level, and sunlight hours."""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1 or water_level > 10:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)")
    else:
        print(f"{plant_name} is healthy!")


def test_plant_checks() -> None:
    """Runs tests for the plant health checker function."""
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        check_plant_health("Tomato", 5, 6)
    except ValueError as e:
        print("Error:", e)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print("Error:", e)
    print("\nTesting bad water level...")
    try:
        check_plant_health("Lettuce", 15, 6)
    except ValueError as e:
        print("Error:", e)
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("Carrots", 5, 0)
    except ValueError as e:
        print("Error:", e)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
