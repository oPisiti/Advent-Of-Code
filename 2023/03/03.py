"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import re


def sum_part_num():
    with open("input.txt") as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    # The coordinates of the special chars
    coords = get_coordinates(data)
 
    # Joining all adjacent numbers into a single list
    adj_numbers = []
    for c in coords:
        adj_numbers += get_adj_numbers(data, c)

    # return adj_numbers
    return sum(adj_numbers)


def get_coordinates(data: list) -> list:
    coords = []

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            # Not special chars
            if char == ".": continue 
            
            try:
                # Is a number
                a = int(char)
            except ValueError as e:
                # IS a special char
                coords.append((i, j))

    return coords


def get_adj_numbers(data: list, coord: tuple) -> list:
    # Defining the base search ranges
    i_range = [coord[0]-1, coord[0], coord[0]+1]
    j_range = [coord[1]-1, coord[1], coord[1]+1]

    # Filtering bad values
    i_range = list(filter(lambda x: x>=0 and x < len(data), i_range))
    j_range = list(filter(lambda x: x>=0 and x < len(data[1]), j_range))

    # Getting the numbers:
    nums = []
    searched_range = set()     # To avoid writing the same number twice
    for i in i_range:
        searched_range.clear()
        for j in j_range:
            if j in searched_range: continue

            n, s = search_num(data, (i, j))
            searched_range.update(s)

            n = int(n)
            if n != 0: nums.append(n)

    return nums


def search_num(data: list, coord: tuple) -> (int, set):
    try:
        int(data[coord[0]][coord[1]])
    except ValueError as e:
        return 0, set()

    num_string = ""
    searched_list = set()

    # Left search
    j = coord[1]
    while j >= 0:
        searched_list.add(j)

        char = data[coord[0]][j]
        try:
            int(char)
            num_string = char + num_string

        except ValueError as e:
            break
        
        j -= 1

    # Right search
    j = coord[1] + 1
    while j < len(data[coord[0]]):
        searched_list.add(j)

        char = data[coord[0]][j]
        try:
            int(char)
            num_string = num_string + char

        except ValueError as e:
            break
        
        j += 1

    return num_string if num_string != "" else 0, searched_list


if __name__ == '__main__':
    print(sum_part_num())
