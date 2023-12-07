"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import re

def scratchcards_points():
    with open("input.txt") as f:
        data = f.read().split("\n")

    data = [numbers.split(":")[-1].strip() for numbers in data]
    data = [numbers.split(" | ") for numbers in data]
    data = [[set(re.findall("\d+", nums)) for nums in card] for card in data]

    total_points = 0
    for cards in data:
        count = len(cards[0].intersection(cards[1]))
        
        if count == 0: continue
        
        total_points += 2**(count-1)

    return total_points        


if __name__ == '__main__':
    print(scratchcards_points())
