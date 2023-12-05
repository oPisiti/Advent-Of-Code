def main():
    elfCalories = []
    with open("input.txt", "r") as cal:
        elfCalories = cal.read().split("\n\n")

    aCal = [elfCalories[i].split("\n") for i in range(len(elfCalories))]

    maxCalories = 0
    for elf in aCal:
        sumCalories = 0
        for snack in elf:
            sumCalories += int(snack)
        maxCalories = max(maxCalories, sumCalories)
    print(maxCalories)


if __name__ == '__main__':
    main()