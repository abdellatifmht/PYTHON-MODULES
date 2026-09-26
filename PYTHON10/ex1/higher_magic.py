from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence_spell


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def ice_blast(target: str, power: int) -> str:
        return f"Ice Blast freezes {target} with {power} power"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result1, result2 = combined("Dragon", 50)
    print(f"Combined spell result: {result1}, {result2}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Goblin', 10)}", end=" ")
    print(f", Amplified: {mega_fireball('Goblin', 10)}")

    print("\nTesting conditional caster...")

    def high_power_only(target: str, power: int) -> bool:
        return power >= 50

    conditional_fire = conditional_caster(high_power_only, fireball)
    print(f"With power 60: {conditional_fire('Troll', 60)}")
    print(f"With power 30: {conditional_fire('Troll', 30)}")

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, ice_blast, heal])
    results = combo("Boss", 40)
    print("Spell sequence results:")
    for i, result in enumerate(results, 1):
        print(f"  {i}. {result}")


if __name__ == "__main__":
    main()
