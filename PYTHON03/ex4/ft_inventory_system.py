import sys


def parse_inventory(args: list) -> dict:
    """Parse inventory items from command-line arguments."""
    inventory = dict()
    for arg in args:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
        else:
            item, quantity_str = arg.split(':', 1)
            try:
                quantity = int(quantity_str)
                if item in inventory:
                    print(f"Redundant item '{item}' - discarding")
                else:
                    inventory[item] = quantity
            except ValueError as e:
                print(f"Quantity error for '{item}': {e}")
    return inventory


def main() -> None:
    """Main function to demonstrate inventory management."""
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 ft_inventory_system.py" +
              " item1:quantity1 item2:quantity2 ...")
        return
    inventory = parse_inventory(args[1:])
    if not inventory:
        print("No valid inventory items provided.")
        return

    print(f"Got inventory: {inventory}")
    items_list = list(inventory.keys())
    print(f"Item list: {items_list}")

    total_items = len(items_list)
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {total_items} items: {total_quantity}")

    for item, quantity in inventory.items():
        percentage = (quantity / total_quantity) * 100
        print(f"Item {item} represents {round(percentage, 1)}%")

    most_abundant = dict()
    least_abundant = dict()
    for item, quantity in inventory.items():
        if not most_abundant or quantity > most_abundant['quantity']:
            most_abundant = {'item': item, 'quantity': quantity}
        if not least_abundant or quantity < least_abundant['quantity']:
            least_abundant = {'item': item, 'quantity': quantity}

    print(f"Item most abundant: {most_abundant['item']}"
          f" with quantity {most_abundant['quantity']}")

    if least_abundant['item'] != most_abundant['item']:
        print(f"Item least abundant: {least_abundant['item']}"
              f" with quantity {least_abundant['quantity']}")

    new_item = {'magic_item': 1}
    inventory.update(new_item)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
