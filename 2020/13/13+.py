import re

def main():
    with open("input.txt") as data:
        d = data.read().splitlines()

    busses = [int(bus) for bus in re.findall("\d+", d[1])]

    dArray = []
    for bus in busses:
        partial = arrive/bus
        dArray.append((1 - partial%1)*bus)

    earliestIndex = dArray.index(min(dArray))
    print(round(busses[earliestIndex] * dArray[earliestIndex]))


if __name__ == '__main__':
    main()