# Returns index of found item
def binSearch(li, item):
    minIndex, maxIndex = 0, len(li)-1
    probeIndex = int((minIndex + maxIndex)/2)

    while minIndex <= maxIndex:

        if li[probeIndex] == item:    return probeIndex
        if minIndex == maxIndex:      ValueError(f"This list does not contain the value {item}") 

        if   li[probeIndex] > item:   maxIndex = probeIndex - 1
        elif li[probeIndex] < item:   minIndex = probeIndex + 1
        
        probeIndex = int((minIndex + maxIndex)/2)

    raise ValueError(f"This list does not contain the value {item}")

# Returns the index of the list which contains the item as its first element
def findItem(li, item):
    for i, sublist in enumerate(li):
        if sublist[0] == item: return i
    
    raise ValueError(f"This list does not contain the value {item}")

# Recursivly solves the answer for a given monkey name
def solve(mName:str, mList:list, mOnlyNames:list):
    # Finding mName index
    mIndex = binSearch(mOnlyNames, mName)

    # Operations
    if type(mList[mIndex][1]) is not list: return  float(mList[mIndex][1])
    
    a = solve(mList[mIndex][1][0], mList, mOnlyNames)
    b = solve(mList[mIndex][1][2], mList, mOnlyNames)

    match mList[mIndex][1][1]:
        case "*": return a * b 
        case "/": return a / b
        case "+": return a + b
        case "-": return a - b


def main():
    # Getting and cleaning data
    with open("input.txt") as data:
        monkeys = data.read().splitlines()

    for i, monkey in enumerate(monkeys):
        monkeys[i] = monkey.split(": ")
        if not monkeys[i][1].isnumeric():
            monkeys[i] = [monkeys[i][0], monkeys[i][1].split(" ")]

    monkeys.sort(key=lambda li: li[0])
    onlyNames = [monk[0] for monk in monkeys]

    print(solve("root", monkeys, onlyNames))


if __name__ == "__main__":
    main()