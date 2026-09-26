from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    creatures = [
        factory.create_base(),
        factory.create_evolved()
    ]
    for creature in creatures:
        print(creature.describe())
        print(creature.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    creatures = [
        factory1.create_base(),
        factory2.create_base(),
    ]
    print(f"{creatures[0].describe()}\n vs.\n{creatures[1].describe()}")
    print(" fight!")
    for creature in creatures:
        print(creature.attack())


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame)
    print()
    test_factory(aqua)
    print()
    test_battle(flame, aqua)


if __name__ == "__main__":
    main()
