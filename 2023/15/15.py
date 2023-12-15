"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

def hash():
    with open("input.txt") as f:
        data = f.read().strip().split(",")

    hash_value = 0
    for step in data:
        curr_value = 0

        for char in step:
            curr_value += ord(char)
            curr_value *= 17
            curr_value %= 256
        
        hash_value += curr_value

    return hash_value    


if __name__ == '__main__':
    print(hash())