"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import re


def cosmic_expansion():
    with open("input.txt") as f:
        uni_raw = f.read().strip().split("\n")

    uni = [re.findall(".", line) for line in uni_raw]

    expand(uni)

    # Getting '#' positions
    galaxies_indexes = []
    for i in range(len(uni)):
        for j in range(len(uni[0])):
            if uni[i][j] == "#": galaxies_indexes.append((i, j))

    # Defining the pairs
    pairs = []
    for f in range(len(galaxies_indexes)):
        for s in range(f+1, len(galaxies_indexes)):
            pairs.append((galaxies_indexes[f], galaxies_indexes[s]))

    # Calculating all the distances
    dist_sum = 0
    for f, s in pairs:
        dist_sum += abs(f[0] - s[0]) + abs(f[1] - s[1])

    return dist_sum


def expand(uni: list[list[str]]) -> None:
    """ Applies universe expansion """

    # Vertical expansion
    j_add_list = []
    for j in range(len(uni[0])):
        clean = True
        for i in range(len(uni)):
            if uni[i][j] == "#":
                clean = False
                break
        
        if clean: j_add_list.append(j)
    
    # Adding vertical expansion
    for j in j_add_list[::-1]:
        for i in range(len(uni)):
            uni[i].insert(j + 1, ".")

    # Horizontal expansion
    i_add_list = []
    for i in range(len(uni)):
        for j in range(len(uni[0])):
            clean = True
            if uni[i][j] == "#":
                clean = False
                break
        
        if clean: i_add_list.append(i)
    
    # Adding vertical expansion
    for i in i_add_list:
        uni.insert(i+1, ["." for _ in range(len(uni[0]))])


if __name__ == '__main__':
    print(cosmic_expansion())