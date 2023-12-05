import re

def notValidField(tick: list[str], tickFields: list[list[list[str]]]):
    for ticket in tick:
        foundPlace = False
        for i, tf in enumerate(tickFields):
            if (ticket > tf[0][0] and ticket < tf[0][1]) or (ticket > tf[1][0] and ticket < tf[1][1]):
                foundPlace = True
                break
        
        if not foundPlace: return ticket

    return 0

def countInvalidTickets():
    with open("input.txt") as data:
        fullData = data.read().split("\n\n")
    
    # Getting and cleaning data
    ticketFields =  [re.findall("\d+-\d+", string) for string in fullData[0].splitlines()]
    for i, field in enumerate(ticketFields):
        for j in range(len(field)):
            ticketFields[i][j] = [int(ans) for ans in re.split("-", ticketFields[i][j])]

    myTicket =      [int(ans) for ans in re.findall("\d+", fullData[1])]
    nearbyTickets = [[int(ans) for ans in re.findall("\d+", string)] for string in fullData[2].splitlines()[1:]]

    # Counting invalid tickets
    validTicketsIndex = [i for i in range(len(nearbyTickets))]
    for i, ticket in enumerate(nearbyTickets):
        validTicketsIndex = validTicketsIndex[:i] + validTicketsIndex[i+1:]



if __name__ == '__main__':
    countInvalidTickets()