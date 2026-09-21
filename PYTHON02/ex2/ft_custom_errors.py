#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when there is an issue with a plant."""
    pass


class WaterError(GardenError):
    """Raised when there is an issue with water levels."""
    pass


def check_plant(plant: str, age: int) -> None:
    if age > 100:
        raise PlantError(f"The {plant} plant is wilting!")


def check_water(water_level: int) -> None:
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


def test_error_types() -> None:
    print("Testing PlantError...")
    try:
        check_plant("tomato", 150)
    except PlantError as e:
        print("Caught PlantError:", e)
    print("\nTesting WaterError...")
    try:
        check_water(5)
    except WaterError as e:
        print("Caught WaterError:", e)
    print("\nTesting catching all garden errors...")
    try:
        check_plant("tomato", 150)
    except GardenError as e:
        print("Caught a GardenError:", e)
    try:
        check_water(5)
    except GardenError as e:
        print("Caught a GardenError:", e)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_error_types()
    print("\nAll custom error types work correctly!")
