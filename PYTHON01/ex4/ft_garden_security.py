class SecurePlant:
    """A class representing a plant in the garden with
    security checks for negative values."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new plant with its name, height in cm,
        and age in days, with security checks for negative values."""
        self.name = name
        if height > 0:
            self.__height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            self.__height = 0
        if age > 0:
            self.__age = age
        else:
            print(f"Invalid operation attempted: age {age} years [REJECTED]")
            print("Security: Negative age rejected")
            self.__age = 0
        print(f"Plant created: {self.name}")

    def set_height(self, height: int) -> None:
        """Set the plant's height with a security check for negative values."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print("Height updated:", height, "cm [OK]")

    def set_age(self, age: int) -> None:
        """Set the plant's age with a security check for negative values."""
        if age < 0:
            print(f"Invalid operation attempted: age {age} years [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print("Age updated:", age, "years [OK]")

    def get_height(self) -> int:
        """Get the plant's height."""
        return self.__height

    def get_age(self) -> int:
        """Get the plant's age."""
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 30, 2)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.name} ({rose.get_height()}cm, "
          f"{rose.get_age()} days)""")
