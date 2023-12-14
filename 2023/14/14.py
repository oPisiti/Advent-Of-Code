"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

def rocks():
    with open("input.txt") as f:
        data = f.read().strip().splitlines()

    platform = [[item for item in row] for row in data]

    # Tilting north
    for i in range(1, len(platform)):
        for j in range(len(platform[0])):
            # Is a moveable rock
            if platform[i][j] == "O":
                move_rocks_north(platform, i, j)
        
        pass

    # Calculating the score
    score = sum([line.count("O") * (len(platform) - i) for i, line in enumerate(platform)])

    return score


def move_rocks_north(plat: list[list[str]], i: int, j: int) -> None:
    i_target = i - 1

    # Determining the end location
    while i_target >= 0:
        if plat[i_target][j] in ("#", "O"):
            i_target += 1
            break

        i_target -= 1

    i_target = max(i_target, 0)

    plat[i][j] = "."
    plat[i_target][j] = "O"


if __name__ == '__main__':
    print(rocks())