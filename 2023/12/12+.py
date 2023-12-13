"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

from functools import cache

def hot_springs() -> int:
    with open("input.txt") as f:
        data = [d.split(" ") for d in f.read().strip().split("\n")]

    expansion = 5
    strips = [("?".join([d[0]] * expansion) + ".", tuple(int(n) for n in d[1].split(",")) * expansion) for d in data]

    count = 0
    for strip in strips:
        count += num_solutions(strip[0], strip[1])

    return count

@cache
def num_solutions(string: str, sizes: tuple[int], branch_count: int = 0) -> int:
    # Branch has ended
    if not string:
        if not sizes and not branch_count: return 1
        return 0

    count = 0

    curr_strings = [".", "#"] if string[0] == "?" else [string[0]]
    for s in curr_strings:
        # Match
        if s == "#": count += num_solutions(string[1:], sizes, branch_count + 1)
        
        # Not a match
        else:            
            # Just after a group
            if branch_count:

                # Group has the appropriate size
                if sizes and branch_count == sizes[0]:
                    count += num_solutions(string[1:], sizes[1:])
            
                # Wrong group size
                else: continue

            # Multiple "." - Move on
            else: count += num_solutions(string[1:], sizes)

    return count


if __name__ == '__main__':
    print(hot_springs())