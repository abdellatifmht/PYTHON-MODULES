#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for garden-related exceptions."""
    pass


class PlantError(GardenError):
    """Raised when there is an issue with a plant."""
    pass


class WaterError(GardenError):
    """Raised when there is an issue with water supply."""
    pass


def check_plant(plant: str, age: int) -> None:
    """Checks the health of a plant and raises a PlantError if it's wilting."""
    if age > 100:
        raise PlantError(f"The {plant} plant is wilting!")


def check_water(water_level: int) -> None:
    """Checks the water level and raises a WaterError if it's insufficient."""
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


class Plant:
    """Represents a plant in the garden."""
    def __init__(
                self,
                name: str,
                age: int,
                water_level: int,
                sunlight_hours: int
                ) -> None:
        """Initializes a Plant with a name, age, water level
        and sunlight hours."""
        self.name = name
        self.age = age
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager():
    def __init__(self, plants: list[Plant]) -> None:
        """Initializes the GardenManager with a list of
        plants and a water level."""
        self.plants = []
        self.water_level = 2

    def add_plant(self, plant: Plant) -> None:
        """Adds a plant to the garden, checking for validity and
        raising PlantError if invalid."""
        if not plant:
            raise PlantError("Plant cannot be None!")
        if not plant.name:
            raise PlantError("Plant name cannot be empty!")
        else:
            self.plants += [plant]
            print(f"Added {plant.name} successfully")

    def water_plants(self) -> None:
        """"Waters all plants in the garden, checking for water
        level and raising WaterError if insufficient."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.water_level < 1:
                    raise WaterError("Not enough water in tank!")
                print(f"Watering {plant.name} - success")
                plant.water_level += 1
                self.water_level -= 1
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        """Checks the health of all plants in the garden, raising
        ValueError for any issues found."""
        for plant in self.plants:
            try:
                if not plant.name:
                    raise ValueError("Plant name cannot be empty!")
                if plant.water_level < 1 or plant.water_level > 10:
                    if plant.water_level < 1:
                        raise ValueError(f"Water level {plant.water_level} "
                                         f"is too low (min 1)")
                    if plant.water_level > 10:
                        raise ValueError(f"Water level {plant.water_level} "
                                         f"is too high (max 10)")
                if plant.sunlight_hours < 2 or plant.sunlight_hours > 12:
                    if plant.sunlight_hours < 2:
                        raise ValueError(f"Sunlight hours "
                                         f"{plant.sunlight_hours} "
                                         f"is too low (min 2)")
                    if plant.sunlight_hours > 12:
                        raise ValueError(f"Sunlight hours "
                                         f"{plant.sunlight_hours} "
                                         f"is too high (max 12)")
                else:
                    print(f"{plant.name}: healthy "
                          f"(water: {plant.water_level}, "
                          f"sun: {plant.sunlight_hours})")
            except ValueError as e:
                print(f"Error checking {plant.name}:", e)

    def error_recovery(self) -> None:
        """Simulates an error recovery process, raising GardenError if
        recovery fails."""
        if self.water_level < 1:
            raise GardenError("Not enough water in tank")
        else:
            print("Water level is sufficient, no recovery needed")


def test_garden_management() -> None:
    """Tests the GardenManager class and its error handling capabilities."""
    print("=== Garden Management System ===\n")
    manager = GardenManager([])
    plants = [
        Plant("tomato", 1, 5, 8),
        Plant("lettuce", 2, 15, 6),
        Plant("", 3, 7, 10),
        ]
    print("Adding plants to garden...")
    try:
        for plant in plants:
            manager.add_plant(plant)
    except PlantError as e:
        print("Error adding plant:", e)
    print("\nWatering plants...")
    try:
        manager.water_plants()
    except ValueError as e:
        print("Error: Cannot water None -", e)
    except WaterError as e:
        print("Caught WaterError:", e)
    print("\nChecking plant health...")
    manager.check_health()
    print("\nTesting error recovery...")
    try:
        manager.error_recovery()
    except GardenError as e:
        print("Caught GardenError:", e)
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
