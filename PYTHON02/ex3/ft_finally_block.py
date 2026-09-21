#!/usr/bin/env python3

class Plant:
    """Represents a plant in the garden."""
    def __init__(self, name: str, age: int, water_level: int) -> None:
        """Initializes a Plant with a name, age, and water level."""
        self.name = name
        self.age = age
        self.water_level = water_level


def water_plants(plant_list: list[Plant]) -> None:
    """Waters a list of plants,
    demonstrating the use of finally for cleanup."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise ValueError("Invalid plant!")
            print(f"Watering {plant.name}")
            plant.water_level += 1
    except ValueError as e:
        print(f"Error: Cannot water {plant} -", e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Tests the watering system with normal and
    error cases to demonstrate the use of finally for cleanup."""
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    plants = [
        Plant("tomato", 1, 5),
        Plant("lettuce", 2, 3),
        Plant("carrots", 3, 7)
        ]
    water_plants(plants)
    print("Watering completed successfully!")
    bad_plants = [Plant("tomato", 1, 5), None, Plant("lettuce", 2, 3)]
    print("\nTesting with error...")
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
