def main():
    with open("input.txt") as data:
        couplesLines = data.read().split("\n")

    coupleSep = []
    for couples in couplesLines:
        coupleSep.append(couples.split(","))

    sumContained = 0
    elfA = {"min":0, "max":0}
    elfB = {"min":0, "max":0}
    a, b = 0, 0
    for couple in coupleSep:
        a, b = couple[0].split("-")
        elfA["min"], elfA["max"] = int(a), int(b)
        a, b = couple[1].split("-")
        elfB["min"], elfB["max"] = int(a), int(b)

        if   elfA["min"] >= elfB["min"] and elfA["max"] <= elfB["max"]:    sumContained += 1
        elif elfA["min"] <= elfB["min"] and elfA["max"] >= elfB["max"]:    sumContained += 1

    print(sumContained)


if __name__ == '__main__':
    main()