class Plant:
    """A class representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new plant with its name,
        height in cm, and age in days."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth_height: int = 1) -> None:
        """Increase the plant's height by a specified amount
        (default is 1 cm)."""
        self.height += growth_height


class FloweringPlant(Plant):
    """A class representing a flowering plant in the garden."""
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            is_blooming: bool
            ) -> None:
        """Initialize a new flowering plant with its name,
        height in cm, and age in days."""
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = is_blooming

    def bloom(self) -> str:
        if self.is_blooming:
            return "blooming"
        return ""


class PrizeFlower(FloweringPlant):
    """A class representing a prize-winning flowering plant in the garden."""
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            is_blooming: bool,
            prize: int
            ) -> None:
        """Initialize a new prize-winning flowering plant with its name,
        height in cm, and age in days."""
        super().__init__(name, height, age, color, is_blooming)
        self.prize = prize


class Garden:
    """A class representing a garden, which can contain multiple plants."""
    def __init__(self, owner: str) -> None:
        """Initialize a new garden with its owner's name."""
        self.owner = owner
        self.plants = []


class GardenManager:
    """A class to manage multiple gardens and provide analytics
    on the plants within them."""
    class GardenStats:
        """A nested class to track statistics about the gardens,
        such as total plants and growth."""
        def __init__(self) -> None:
            """Initialize the garden statistics."""
            self.total_plants = {}
            self.total_growth = {}

        def add_plant(self, owner: str) -> None:
            """Add a plant to the statistics for the specified owner."""
            if owner in self.total_plants:
                self.total_plants[owner] += 1
            else:
                self.total_plants[owner] = 1

        def add_growth(self, owner: str, growth: int = 1) -> None:
            """Add growth to the statistics for the specified owner."""
            if owner in self.total_growth:
                self.total_growth[owner] += growth
            else:
                self.total_growth[owner] = growth

        def generate_score(garden: Garden) -> int:
            """Generate a score for a garden based on the heights
            of its plants and any prizes."""
            score = 0
            for plant in garden.plants:
                score += plant.height
                if plant.__class__.__name__ == "PrizeFlower":
                    score += 4 * plant.prize
            return score
        generate_score = staticmethod(generate_score)

    def __init__(self) -> None:
        """Initialize the garden manager with an empty
        collection of gardens and statistics."""
        self.gardens = {}
        self.stats = {}
        self.stats = self.GardenStats()
        self.total_gardens = 0

    def add_garden(self, garden: Garden) -> None:

        """Add a new garden to the manager."""
        self.gardens[garden.owner] = garden.plants
        self.total_gardens += 1

    def add_plant(self, owner: str, plant: Plant) -> None:
        """Add a plant to the manager's statistics."""
        self.stats.add_plant(owner)
        if owner in self.gardens:
            self.gardens[owner] += [plant]
        else:
            self.gardens[owner] = [plant]
        print(f"Added {plant.name} to {owner}'s garden.")

    def grow_plants(self, owner: str, growth_height: int = 1) -> None:
        """Grow all plants in a specific garden by a specified amount."""
        if owner in self.gardens:
            print(f"{owner} is helping all plants grow...")
            for plant in self.gardens[owner]:
                plant.grow(growth_height)
                self.stats.add_growth(owner, growth_height)
                print(f"{plant.name} grew {growth_height}cm.")
        else:
            print(f"No garden found for owner: {owner}")

    def report(self, owner: str) -> None:
        """Generate a report for a specific garden."""
        if owner in self.gardens:
            regular = 0
            flowering = 0
            prize = 0
            print(f"\n=== {owner}'s Garden Report ===")
            print("Plants in garden:")
            for plant in self.gardens[owner]:
                if plant.__class__.__name__ == "Plant":
                    regular += 1
                    print(f"- {plant.name}: {plant.height}cm")
                elif plant.__class__.__name__ == "FloweringPlant":
                    flowering += 1
                    print(f"- {plant.name}: {plant.height}cm, "
                          f"{plant.color} flowers ({plant.bloom()})")
                elif plant.__class__.__name__ == "PrizeFlower":
                    prize += 1
                    print(f"- {plant.name}: {plant.height}cm, "
                          f"{plant.color} flowers ({plant.bloom()}),"
                          f" Prize points: {plant.prize})")
            print(f"\nPlants added: {self.stats.total_plants[owner]},"
                  f" Total growth: {self.stats.total_growth[owner]}cm")
            print(f"Plants types: {regular} regular,"
                  f" {flowering} flowering, {prize} prize flowers")
        else:
            print(f"No garden found for owner: {owner}")

    def validate_height(height: int) -> bool:
        """Validate that the height is a positive integer."""
        return height > 0
    validate_height = staticmethod(validate_height)

    def create_garden_network(cls, gardens: list) -> "GardenManager":
        """Create a network of gardens from a list of Garden instances."""
        network = cls()
        for garden in gardens:
            network.add_garden(garden)
        return network
    create_garden_network = classmethod(create_garden_network)


def main() -> None:
    print("=== Garden Management System Demo ===\n")
    gardens = [
        Garden("Alice"),
        Garden("Bob")
    ]
    plants = [
        Plant("Oak Tree", 100, 365),
        FloweringPlant("Rose", 25, 30, "red", True),
        PrizeFlower("Sunflower", 50, 60, "yellow", True, 10)
    ]
    manager = GardenManager()
    for garden in gardens:
        manager.add_garden(garden)
    for plant in plants:
        manager.add_plant("Alice", plant)
    manager.add_plant("Bob", Plant("Pine Tree", 92, 300))
    print()
    manager.grow_plants("Alice")
    manager.report("Alice")
    print("\nHeight validation test:", manager.validate_height(10))
    print(f"Garden scores - Alice:"
          f" {manager.GardenStats.generate_score(gardens[0])},"
          f" Bob: {manager.GardenStats.generate_score(gardens[1])}")
    print(f"Total gardens managed: {manager.total_gardens}")


if __name__ == "__main__":
    main()
