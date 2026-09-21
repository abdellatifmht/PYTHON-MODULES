class Plant:
    """A class representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with its name, height, and age."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """A class representing a flower, which is a type of plant."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize the flower with its name, height, age, and color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Simulate the blooming of the flower."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """A class representing a tree, which is a type of plant."""
    def __init__(self, name: str, height:
                 int, age: int, trunk_diameter: int) -> None:
        """Initialize the tree with its name, height, age,
        and trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, shade: int) -> None:
        """Simulate the tree providing shade."""
        print(f"{self.name} provides {shade} square meters of shade.")


class Vegetable(Plant):
    """A class representing a vegetable, which is a type of plant."""
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        """Initialize the vegetable with its name, height, age, harvest season,
        and nutritional value."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    flowers = (
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "yellow"),
    )
    trees = (
        Tree("Oak", 500, 100, 50),
        Tree("Pine", 300, 80, 30),
    )
    vegetables = (
        Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C"),
        Vegetable("Carrot", 15, 60, "spring", "high in Vitamin A"),
    )

    print("=== Garden Plant Types ===")
    for flower in flowers:
        print(f"\n{flower.name} (Flower): {flower.height}cm, {flower.age}"
              f" days, {flower.color} color")
        flower.bloom()
    for tree in trees:
        print(f"\n{tree.name} (Tree): {tree.height}cm, {tree.age} days,"
              f" {tree.trunk_diameter}cm diameter")
        tree.produce_shade(78)
    for vegetable in vegetables:
        print(f"\n{vegetable.name} (Vegetable): {vegetable.height}cm,"
              f" {vegetable.age} days,"
              f" {vegetable.harvest_season} harvest")
        print(f"{vegetable.name} is {vegetable.nutritional_value}")
