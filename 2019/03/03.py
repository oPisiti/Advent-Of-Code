import re
import numpy as np


def main():
    # Getting data
    with open("input.txt") as data:
        wireA, wireB = data.read().split("\n")

    wireA = wireA.split(",")
    wireA = [[a[0], int(a[1:])] for a in wireA]
    wireB = wireB.split(",")
    wireB = [[b[0], int(b[1:])] for b in wireB]

    # Determining the maximum and minimum for i and j
    j_dir = {"R", "L"}
    j_listA = [command[1] for command in wireA if command[0] in j_dir]
    j_listB = [command[1] for command in wireB if command[0] in j_dir]
    j_list = sorted(j_listA + j_listB)

    i_dir = {"U", "D"}
    i_listA = [command[1] for command in wireA if command[0] in i_dir]
    i_listB = [command[1] for command in wireB if command[0] in i_dir]
    i_list = sorted(i_listA + i_listB)

    min_i, max_i = i_list[0], i_list[-1]
    min_j, max_j = j_list[0], j_list[-1]

    # Initializing tables
    i_len, j_len = max_i - min_i, max_j - min_j
    tableA = np.zeros((i_len, j_len), dtype=np.bool_)
    tableB = np.zeros((i_len, j_len), dtype=np.bool_)

    print(f"{tableA}")


if __name__ == "__main__":
    main()
