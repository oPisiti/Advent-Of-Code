def main():
    elfCalories = []
    with open("input.txt", "r") as cal:
        elfCalories = cal.read().split("\n\n")

    aCal = [elfCalories[i].split("\n") for i in range(len(elfCalories))]

    top3Elves = [0, 0, 0]
    for elf in aCal:
        partialCalories = 0
        for snack in elf:
            partialCalories += int(snack)
        
        top3Elves[0] = max(top3Elves[0], partialCalories)
        top3Elves.sort()

    sumCalories = sum(top3Elves)    
    print(sumCalories)


if __name__ == '__main__':
    main()