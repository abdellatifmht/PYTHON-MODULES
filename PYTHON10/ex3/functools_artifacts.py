from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == 'add':
        return reduce(operator.add, spells)
    if operation == 'multiply':
        return reduce(operator.mul, spells)
    if operation == 'max':
        return max(spells)
    if operation == 'min':
        return min(spells)

    raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable]:
    return {
        'fire_enchant': partial(base_enchantment, 50, 'fire'),
        'ice_enchant': partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': partial(base_enchantment, 50, 'lightning')
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast_spell(spell: Any) -> str:
        return f"Unknown spell type: {type(spell).__name__}"

    @cast_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast_spell.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    @cast_spell.register(float)
    def _(spell: float) -> str:
        return f"Precision spell: {spell:.2f} power"

    return cast_spell


def main() -> None:
    print("\nTesting spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print(f"Min: {spell_reducer(powers, 'min')}")

    print("\nTesting partial enchanter...")

    def base_enchant(power: int, element: str, target: str) -> str:
        return (
            f"{element.capitalize()} enchantment "
            f"on {target} with {power} power"
        )

    enchantments = partial_enchanter(base_enchant)
    print(enchantments['fire_enchant']('sword'))
    print(enchantments['ice_enchant']('shield'))
    print(f"Type check: {type(enchantments['fire_enchant'])}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))
    print(dispatcher({"type": "unknown"}))


if __name__ == "__main__":
    main()
