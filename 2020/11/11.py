from timeMe import timeMe

def getMaxSupportedValuesMatrix(seats, current):
    return len(seats[current])-1, len(seats[current][0])-1

def countSeats(seats, current, x, y):
    iMax, jMax = getMaxSupportedValuesMatrix(seats, current)

    count = {
        "empty":    0,
        "occupied": 0 
    }

    for i in range(x-1, x+2):
        if i < 0 or i > iMax: continue

        for j in range(y-1, y+2):
            if j < 0 or j > jMax: continue
            if i == x and j == y: continue

            if   seats[current][i][j] == "L":   count["empty"]    += 1
            elif seats[current][i][j] == "#":   count["occupied"] += 1

    return count

def applyIteration(seats, current):
    other = (current + 1)%2

    iMax, jMax = getMaxSupportedValuesMatrix(seats, current)
    for i in range(iMax+1):
        row = ""
        for j in range(jMax+1):
            count = countSeats(seats, current, i, j)

            if   seats[current][i][j] == "L" and count["occupied"] == 0:    row += "#"
            elif seats[current][i][j] == "#" and count["occupied"] >= 4:    row += "L"
            else:                                                           row += seats[current][i][j]

        seats[other][i] = row


def countOccSeats(seats, current):
    iMax, jMax = getMaxSupportedValuesMatrix(seats, current)
    count = 0
    for i in range(iMax+1):
        for j in range(jMax+1):
            if seats[current][i][j] == "#": count += 1

    return count

@timeMe
def Conway():
    currentSeats = 0

    seats = []

    with open("input.txt") as data:
        seats.append(data.read().split("\n"))

    seats.append(["."*len(seats[0][0]) for i in range(len(seats[0]))])

    c = 1
    while True:
        applyIteration(seats, currentSeats)

        if seats[0] == seats[1]:
            print(f"Stabilized with {countOccSeats(seats, currentSeats)} occupied seats after {c} iterations")
            return
            # print(seats[0])
            # print()
            # print(seats[1])

        currentSeats = (currentSeats + 1)%2
        c += 1


if __name__ == '__main__':
    Conway()