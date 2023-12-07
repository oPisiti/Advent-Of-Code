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

    cards_count = [1 for i in range(len(data))]

    for i, cards in enumerate(data):
        count = len(cards[0].intersection(cards[1]))
        
        if count == 0: continue
        
        # Card has matching numbers
        for j in range(count):
            cards_count[i+j+1] += 1 * cards_count[i]
        
        pass

    return sum(cards_count)        


if __name__ == '__main__':
    print(scratchcards_points())
