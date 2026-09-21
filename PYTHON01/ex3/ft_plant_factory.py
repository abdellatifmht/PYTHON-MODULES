class Plant:
    """A class representing a plant in the garden."""
    plant_count = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new plant with its name, height in cm,
        and age in days."""
        self.name = name
        self.height = height
        self.age_plant = age
        Plant.plant_count += 1

    def get_info(self) -> None:
        """Display the plant's information."""
        print(f"Created: {self.name} ({self.height}cm, {self.age_plant} days)")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.get_info()
    print(f"\nTotal plants created: {Plant.plant_count}")
