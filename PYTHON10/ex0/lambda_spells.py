from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact['power'],
        reverse=True
    )


def power_filter(
    mages: list[dict[str, Any]],
    min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    powers = [mage['power'] for mage in mages]
    return {
        'max_power': max(powers, key=lambda p: p),
        'min_power': min(powers, key=lambda p: p),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


def main() -> None:
    print("\nTesting artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'magic'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Ice Ring', 'power': 78, 'type': 'jewelry'},
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    first_artifact = sorted_artifacts[0]
    second_artifact = sorted_artifacts[1]
    print(
        f"{first_artifact['name']} ({first_artifact['power']} power) "
        f"comes before {second_artifact['name']} "
        f"({second_artifact['power']} power)"
    )

    print("\nTesting power filter...")
    mages = [
        {'name': 'Gandalf', 'power': 95, 'element': 'light'},
        {'name': 'Saruman', 'power': 88, 'element': 'shadow'},
        {'name': 'Radagast', 'power': 72, 'element': 'nature'},
    ]
    powerful_mages = power_filter(mages, 80)
    print(f"Mages with power >= 80: {[m['name'] for m in powerful_mages]}")

    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(' '.join(transformed))

    print("\nTesting mage statistics...")
    stats = mage_stats(mages)
    print(f"Max Power: {stats['max_power']}")
    print(f"Min Power: {stats['min_power']}")
    print(f"Avg Power: {stats['avg_power']}")


if __name__ == "__main__":
    main()
