def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    capitalised_seed = seed_type.capitalize()
    if unit == "packets":
        print(capitalised_seed, "seeds:", quantity, unit, "available")
    elif unit == "grams":
        print(capitalised_seed, "seeds:", quantity, unit, "total")
    elif unit == "area":
        print(capitalised_seed, "seeds: covers",
              quantity, unit, "square meters")
    else:
        print("Unknown unit type")
