"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""


class Index2D:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

    def __add__(self, other):
        if type(other) == Index2D:
            return Index2D(self.i + other.i, self.j + other.j)

        return Index2D(self.i + other[0], self.j + other[1])

    def __sub__(self, other):
        if type(other) == Index2D:
            return Index2D(self.i - other.i, self.j - other.j)

        return Index2D(self.i - other[0], self.j - other[1])
    
    def __eq__(self, other) -> bool:
        if type(other) != Index2D: return False

        return self.i == other.i and self.j == other.j

    def __repr__(self) -> str:
        return f"({self.i}, {self.j})"
        

def gardener() -> int:
    # Constants
    steps = 64

    # Input and parsing
    with open("input.txt") as f:
        data = f.read().strip().split("\n")

    garden = [[char for char in line] for line in data]
    
    # Determining the start position
    s_pos = None
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if garden[i][j] == "S":
                s_pos = Index2D(i, j)
                break
        
        if s_pos: break

    # Marking S as position 0
    garden[s_pos.i][s_pos.j] = "0"

    # Only the border will be kept track of
    border = [s_pos]

    # Determining the possible positions
    symbols = ["0", "1"]
    count = 0
    while count < steps:
        new_border = []

        for b in border:
            new_border += march(garden, b, symbols[(count+1)%2])

        border = new_border
        count += 1

    return sum([sum([c == symbols[(count)%2] for c in line]) for line in garden])


def march(garden: list[list[str]], pos: Index2D, symbol: str) -> list:
    changed_pos = []

    for d in (Index2D(1, 0), Index2D(0, 1), Index2D(-1, 0), Index2D(0, -1)):
        next_pos = pos + d

        # Out of bounds
        if not (0 <= next_pos.i < len(garden)) or not (0 <= next_pos.i < len(garden[0])):
            continue

        # Valid position
        if garden[next_pos.i][next_pos.j] == ".":
            garden[next_pos.i][next_pos.j] = symbol
            changed_pos.append(next_pos)

    return changed_pos


if __name__ == '__main__':
    print(gardener())