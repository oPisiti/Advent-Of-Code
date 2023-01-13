def countTrees():
    with open("input.txt") as data:
        terrain = data.read().split("\n")

    right, down = 3, 1
    wide = len(terrain[0])
    countTrees = 0
    j = 0

    for i in range(0, len(terrain), down):
        if terrain[i][j] == "#": countTrees += 1
        j = (j+right)%wide

    print(f"Encountered {countTrees} trees")


if __name__ == "__main__":
    countTrees()