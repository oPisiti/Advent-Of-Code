def getRow(code:str):
    probeA, probeB = 0, 127

    for i in range(len(code)-1):
        nex = int((probeA + probeB)/2)
        if code[i] == "F":  probeB = nex
        else:               probeA = nex + 1

    if code[-1] == "F":     return probeA
    else:                   return probeB

def getColumn(code:str):
    probeA, probeB = 0, 7

    for i in range(len(code)-1):
        nex = int((probeA + probeB)/2)
        if code[i] == "L":  probeB = nex
        else:               probeA = nex + 1

    if code[-1] == "L":     return probeA
    else:                   return probeB

def highestSeatID():
    with open("input.txt") as data:
        seats = data.read().splitlines()
    
    seats = [[seat[:7], seat[7:]] for seat in seats]

    IDs = []
    for seat in seats:
        row, column = getRow(seat[0]), getColumn(seat[1])
        IDs.append(row * 8 + column)
    
    IDs.sort()
    for i in range(0, len(IDs)-2, 1):
        if IDs[i+1]-1 != IDs[i]:
            print(f"My ID: {IDs[i] + 1}")
            return

    print(f"ID not found")


if __name__ == '__main__':
    highestSeatID()