def main():
    guide = []
    with open("input.txt", "r") as data:
        guide = data.read().split("\n")

    rounds = [guideLine.split(" ") for guideLine in guide]
    
    # Translating XYZ -> ABC
    for i in range(len(rounds)):
        match rounds[i][1]:
            case "X":
                rounds[i][1] = "A"
                continue
            case "Y":
                rounds[i][1] = "B"
                continue
            case "Z":
                rounds[i][1] = "C"
                continue

    winsOver = {
        "A": "C",
        "C": "B",
        "B": "A",
    }

    chooseScore = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    # Calculating the score 
    score = 0
    for r in rounds:
        # Win/draw points
        if   r[0] == winsOver[r[1]]: score += 6     # I win
        elif r[0] == r[1]:           score += 3     # Draw   

        # Bonus points for choice
        score += chooseScore[r[1]]

    print(f"My final score is: {score}")


if __name__ == '__main__':
    main()


