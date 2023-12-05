import numpy as np

def simple_overlapping(li: list[list]) -> int:
    count = 0
    



def cout_overlapping_points_simple():
    """
    Counts how many points overlap. 

    Takes into consideration ONLY horizontal and vertical lines.
    """

    with open("input.txt") as data:
        data_lines = data.read().split("\n")

    lines = [row.split(" -> ") for row in data_lines]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            lines[i][j] = lines[i][j].split(",")
    
    # Getting only horizontal or vertical lines
    simple_lines = list(filter(lambda points: points[0][0] == points[1][0] or points[0][1] == points[1][1], lines))

    # print(simple_lines)
    count_overlapping = simple_overlapping()
    print(f"There are {count_overlapping} overlapping points")



if __name__ == '__main__':
    cout_overlapping_points_simple()