import math


def distance_3d(point1: tuple, point2: tuple) -> float:
    """Calculates the distance between two points in 3D space."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def get_player_pos() -> tuple:
    """Prompts the user to enter coordinates
    and returns them as a tuple of floats."""
    try:
        coords = input("Enter new coordinates as floats in format 'x,y,z':")
        x_str, y_str, z_str = coords.split(",")
        try:
            x = float(x_str)
        except ValueError as e:
            print(f"Error on parameter '{x_str.strip()}': {e}'")
            return get_player_pos()
        try:
            y = float(y_str)
        except ValueError as e:
            print(f"Error on parameter '{y_str.strip()}': {e}'")
            return get_player_pos()
        try:
            z = float(z_str)
        except ValueError as e:
            print(f"Error on parameter '{z_str.strip()}': {e}'")
            return get_player_pos()
        return (x, y, z)
    except ValueError:
        print("Invalid syntax")
        return get_player_pos()


def main() -> None:
    """Main function to demonstrate the coordinate system."""
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    try:
        point1 = get_player_pos()
    except KeyboardInterrupt:
        print("\nExiting...")
        return
    print(f"Got a first tuple: {point1}")
    print(f"It includes: X={point1[0]}, Y={point1[1]}, Z={point1[2]}")
    print(f"Distance to center: {round(distance_3d(point1, (0, 0, 0)), 4)}")

    print("\nGet a second set of coordinates")
    try:
        point2 = get_player_pos()
    except KeyboardInterrupt:
        print("\nExiting...")
        return
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(distance_3d(point1, point2), 4)}")


if __name__ == "__main__":
    main()
