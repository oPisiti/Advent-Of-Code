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

    losesOver = {
        "A": "B",
        "C": "A",
        "B": "C",
    }

    chooseScore = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    # Calculating the score 
    score = 0
    for r in rounds:
        myChoice = ""
        match r[1]:
            case "A":           # I need to lose
                myChoice = winsOver[r[0]]
            case "B":           # Draw
                myChoice = r[0]
                score += 3
            case "C":           # I need to win
                myChoice = losesOver[r[0]]
                score += 6

        # Bonus points for choice
        score += chooseScore[myChoice]

    print(f"My final score is: {score}")


if __name__ == '__main__':
    main()


