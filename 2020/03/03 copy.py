def countTrees():
    with open("input.txt") as data:
        terrain = data.read().split("\n")

    slopes = [
        {"right":1, "down" : 1},
        {"right":3, "down" : 1},
        {"right":5, "down" : 1},
        {"right":7, "down" : 1},
        {"right":1, "down" : 2},
    ]

    wide = len(terrain[0])
    product = 1

    for slope in slopes:
        countTrees = 0 
        j = 0
        for i in range(0, len(terrain), slope["down"]):
            if terrain[i][j] == "#": countTrees += 1
            j = (j+slope["right"])%wide

        print(f"Found {countTrees} trees for slope {slope}")
        product *= countTrees

    print(f"Product: {product}")


if __name__ == "__main__":
    countTrees()