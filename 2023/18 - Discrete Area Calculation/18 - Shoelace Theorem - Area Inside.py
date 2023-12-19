"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""


def lavaduct() -> int:
    with open("input.txt") as f:
        data = f.read().strip().split("\n")

    instructions = [[line.split(" ")[0].strip(), int(line.split(" ")[1])] for line in data]

    # Getting the vertices and perimeter area
    curr = [0, 0]
    vertices = [curr.copy()]
    per_area = 0

    for _dir, amount in instructions:
        match _dir:
            case "D": curr[0] += amount
            case "U": curr[0] -= amount
            case "R": curr[1] += amount
            case "L": curr[1] -= amount
        
        per_area += abs(amount)
        vertices.append(curr.copy())

    # Calculating the area
    area = 0
    for i in range(len(vertices) - 1):
        partial_area = (vertices[i+1][1] + vertices[i][1]) * (vertices[i+1][0] - vertices[i][0]) // 2
        area += partial_area

    return abs(area) + 1 + per_area/2


if __name__ == '__main__':
    print(lavaduct())