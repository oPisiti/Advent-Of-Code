# Returns the priority of a letter based on the exercise's description
def getPriority(item):
    ordered = ord(item)
    if ordered < 65 or (ordered > 90 and ordered < 97) or ordered > 122: return -1 

    if ordered >= 97:   return ordered - 96
    elif ordered >= 65: return ordered - 38

# Creates a basic 52 positions array
def resetElfCounter():
    return [0 for i in range(52)]

# Sets items in array to 1 if item appears in list
def countItems(items):
    baseCounter = resetElfCounter()
    
    for item in items:
        baseCounter[getPriority(item)-1] = 1

    return baseCounter

def main():
    sumPriorities = 0

    with open("input.txt", "r") as ruck:
        rucksacks = ruck.read().split("\n")

    for i in range(0, len(rucksacks), 3):
        elfA = countItems(rucksacks[i])
        elfB = countItems(rucksacks[i+1])
        elfC = countItems(rucksacks[i+2])
        
        # Finding the common item in all three elves' packs
        for i in range(52):
            if elfA[i] and elfB[i] and elfC[i]:
                sumPriorities += i+1
                break

    print(sumPriorities)


if __name__ == '__main__':
    main()