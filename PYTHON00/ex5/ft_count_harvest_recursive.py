def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def helper(days, current_day):
        if current_day > days:
            print("Harvest time!")
            return
        print("Day", current_day)
        helper(days, current_day + 1)
    helper(days, 1)
