def ft_water_reminder() -> None:
    last_watered = int(input("Days since last watering: "))
    if last_watered > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
