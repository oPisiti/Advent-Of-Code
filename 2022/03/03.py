def getPriority(item):
    ordered = ord(item)
    if ordered < 65 or (ordered > 90 and ordered < 97) or ordered > 122: return -1 

    if ordered >= 97:   return ordered - 96
    elif ordered >= 65: return ordered - 38

def main():
    sumPriorities = 0

    with open("input.txt", "r") as ruck:
        rucksacks = ruck.read().split("\n")

    for sack in rucksacks:
        firstComp = sack[:int(len(sack)/2)]
        secondComp = sack[int(len(sack)/2):]

        for item in firstComp:
            if item in secondComp:
                print(f"Common item: {item}. Adding {getPriority(item)} points")
                sumPriorities += getPriority(item)
                break
    
    print(sumPriorities)


if __name__ == '__main__':
    main()