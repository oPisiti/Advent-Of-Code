"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import re


class Strip():
    def __init__(self, strip: list[str], sizes: list[int]) -> None:
        self.strip = strip
        self.sizes = sizes
        self.count = 0


    def count_possibilities(self, strip_partial: str = None) -> None:
        if strip_partial is None: strip_partial = self.strip

        indexes = [i for i in range(len(strip_partial)) if strip_partial[i] == "?"]

        complete = False
        if len(indexes) == 0: return
        if len(indexes) == 1: complete = True

        for char in (".", "#"):
            curr_strip = strip_partial[:indexes[0]] + char + strip_partial[indexes[0] + 1:]

            # Too many "#"
            if len([i for i in range(len(strip_partial)) if strip_partial[i] == "#"]) > sum(self.sizes): return

            if complete:
                if self.is_valid_strip(curr_strip): 
                    self.count += 1

            else:        
                self.count_possibilities(curr_strip)  

        return


    def is_valid_strip(self, strip: str) -> bool:
        parts = re.findall("\#+", strip)

        # Too many parts
        if len(parts) != len(self.sizes): return False

        index = 0
        for part in parts:
            if len(part) != self.sizes[index]: return False
            index += 1
        
        return True


def hot_springs():
    with open("input.txt") as f:
        data = [d.split(" ") for d in f.read().strip().split("\n")]

    strips = []
    for i, spring in enumerate(data):
        strips.append(Strip(data[i][0], [int(a) for a in data[i][1].split(",")]))

    # Counting 
    answer = 0
    for strip in strips:
        strip.count_possibilities()
        pass

        answer += 1

    pass
    return sum([strip.count for strip in strips])



if __name__ == '__main__':
    print(hot_springs())