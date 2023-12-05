from timeMe import timeMe

def getMaxSupportedValuesMatrix(seats, current):
    return len(seats[current])-1, len(seats[current][0])-1

def countSeats(seats, current, i, j):

    count = {
        "empty":    0,
        "occupied": 0 
    }

    directions = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    )

    for direct in directions:
        search = searchDirection(seats, current, i, j, direct)
        if   search == "L": count["empty"]    += 1
        elif search == "#": count["occupied"] += 1

    return count


def applyIteration(seats, current):
    other = (current + 1)%2

    iMax, jMax = getMaxSupportedValuesMatrix(seats, current)
    for i in range(iMax+1):
        row = ""
        for j in range(jMax+1):
            count = countSeats(seats, current, i, j)

            if   seats[current][i][j] == "L" and count["occupied"] == 0:    row += "#"
            elif seats[current][i][j] == "#" and count["occupied"] >= 5:    row += "L"
            else:                                                           row += seats[current][i][j]

        seats[other][i] = row

# Counts occupied seats, given a position
def countOccSeats(seats, current):
    iMax, jMax = getMaxSupportedValuesMatrix(seats, current)
    count = 0
    for i in range(iMax+1):
        for j in range(jMax+1):
            if seats[current][i][j] == "#": count += 1

    return count

# Counts all occupied seats in sight line
def searchDirection(seats, current, iInit, jInit, direct):
    i, j = iInit, jInit
    iMax, jMax = getMaxSupportedValuesMatrix(seats, current)

    i += direct[0]
    j += direct[1]
    while i >= 0 and j >= 0 and i <= iMax and j <= jMax:
        seat = seats[current][i][j]
        if seat != ".": return seat

        i += direct[0]
        j += direct[1]  
    
    return "."


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

        currentSeats = (currentSeats + 1)%2
        c += 1


if __name__ == '__main__':
    Conway()