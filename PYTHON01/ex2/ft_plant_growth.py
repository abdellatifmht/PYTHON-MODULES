class Plant:
    """A class representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new plant with its name, height in cm,
        and age in days."""
        self.name = name
        self.height = height
        self.age_plant = age

    def get_info(self) -> None:
        """Display the plant's information."""
        print(f"{self.name}: {self.height}cm, {self.age_plant} days old")

    def grow(self, growth_height: int = 1) -> None:
        """Increase the plant's height by a specified amount
        (default is 1 cm)."""
        self.height += growth_height

    def age(self, growth_age: int = 1) -> None:
        """Increase the plant's age by a specified amount
        (default is 1 day)."""
        self.age_plant += growth_age


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    init_height = rose.height
    print("=== Day 1 ===")
    rose.get_info()
    for _ in range(6):
        rose.grow(1)
        rose.age(1)
        sunflower.grow(2)
        sunflower.age(1)
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose.height - init_height}cm")
