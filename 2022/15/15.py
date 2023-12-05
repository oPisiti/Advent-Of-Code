import re

class Node():
    def __init__(self, x: int, y: int, _next = None) -> None:
        self.x, self.y = x, y
        self.next = _next
    
    def __eq__(self, cmp) -> bool:
        if type(cmp) != Node: raise TypeError

        if self.x == cmp.x and self.y == cmp.y:
            return True
        
        return False

class Range():
    def __init__(self, _min: int, _max: int) -> None:
        self.min = _min
        self.max = _max


def simplify_ranges(ranges: list[Range]) -> list[Range]:
    output = ranges[0]

    for i in range(1, len(ranges)):
        merge_ranges()



def count_impossible_positions_row(row, path="input.txt") -> int:
    with open(path) as data:
        coord = data.read().splitlines()

    coords = [[int(num) for num in re.findall("=(-?\d+)", co)] for co in coord]    
    
    sensors = []
    beacons = []
    for c in coords:
        possible = Node(c[2], c[3])
        if possible not in beacons: beacons.append(possible)

        sensors.append(Node(c[0], c[1], possible)) 

    # Determining where not possible in at a certain row
    row = 10
    a = Range(1, 20)
    b = Range(24, 30)
    ranges_row = simplify_ranges([a, b])
    # for sensor in sensors:
    #     print(sensor + Node(10, 20))

    pass



if __name__ == '__main__':
    count_impossible_positions_row(10)