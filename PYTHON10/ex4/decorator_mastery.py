import time
import functools
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(self: Any, power: int, *args: Any, **kwargs: Any) -> Any:
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, power, *args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            "Spell casting failed "
                            f"after {max_attempts} attempts"
                        )
            return None
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}\n")

    print("Testing retrying spell...")

    @retry_spell(max_attempts=3)
    def always_fails() -> str:
        raise Exception("Always fails")

    print(always_fails())

    @retry_spell(max_attempts=2)
    def complex_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(f"{complex_spell()}\n")

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf the Grey"))
    print(MageGuild.validate_mage_name("X"))

    guild = MageGuild()
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Fireball"))


if __name__ == "__main__":
    main()
