class Plant:
    """A class representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new plant with its name,
        height in cm, and age in days."""
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        """Display the plant's information."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
        ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.display_info()
