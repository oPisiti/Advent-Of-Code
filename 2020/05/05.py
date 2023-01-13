def decodeSeat(code: str, position: str):
    if position != "Row" and position != "Column":
        raise AttributeError("Position not supported")

    probeA, probeB = 0, 128 if position == "Row" else 7
    for letter in code:
        nextPoint = int((probeA + probeB)/2)
        if   letter == "F": probeB = nextPoint
        elif letter == "B": probeA = nextPoint
    
    return probeA

def highestSeatID():
    with open("input.txt") as data:
        seats = data.read().splitlines()
    
    seats = [[seat[:7], seat[7:]] for seat in seats]
    # print(seats)

    highestID = 0
    for seat in seats:
        row, column = decodeSeat(seat[0], "Row"), decodeSeat(seat[1], "Column")
        ID = row * 8 + column
        if ID > highestID: highestID = ID
    
    print(f"Highest ID: {highestID}")


if __name__ == '__main__':
    highestSeatID()