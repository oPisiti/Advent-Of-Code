"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import re


def hot_springs():
    with open("input.txt") as f:
        data = [d.split(" ") for d in f.read().strip().split("\n")]

    for i, spring in enumerate(data):
        data[i][0] = re.findall("[\?\#]+", data[i][0])
        data[i][1] = [int(a) for a in data[i][1].split(",")]
    
    # Counting 
    answer = 0
    for i, spring in enumerate(data):
        len_left = data[i][1].copy()

        arr = 1
        for strip in spring[0]:
            # Full of "#" or "."
            hash_count = len([1 for char in strip if char == "?"])
            if hash_count == 0: continue

            counted = count_possibilities(strip, len_left)
            print(f"Counted: {counted}")
            arr *= counted
            pass

        answer += arr

    pass
    return answer


def count_possibilities(strip: str, lengths: list[int]) -> int:
    indexes = [i for i in range(len(strip)) if strip[i] == "?"]
    
    complete = False
    if len(indexes) == 0: return 0
    if len(indexes) == 1: complete = True

    count = 0

    for char in (".", "#"):
        curr_strip = strip[:indexes[0]] + char + strip[indexes[0] + 1:]

        # Too many "#"
        if len([i for i in range(len(strip)) if strip[i] == "#"]) > sum(lengths): return 0

        if complete:
            is_valid, lengths = is_valid_strip(curr_strip, lengths)

            if is_valid and len(lengths) == 0: count += 1

        else:        
            count += count_possibilities(curr_strip, lengths)  

        pass  


    return count


def is_valid_strip(strip: str, lengths: list[int]) -> (bool, list[int]):
    parts = re.findall("\#+", strip)

    # Too many parts
    if len(parts) > len(lengths): return False, lengths
    if len(parts) == 0:           return False, lengths

    index = 0
    for part in parts:
        if len(part) != lengths[index]: return False, lengths
        index += 1
    
    lengths = lengths[index:]

    return True, lengths


if __name__ == '__main__':
    print(hot_springs())