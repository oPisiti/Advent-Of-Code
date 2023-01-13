from multipledispatch import dispatch

class Point2d():
    @dispatch(int, int)
    def __init__(self, i, j):
        self.i = i
        self.j = j

    @dispatch(str)
    def __init__(self, pos):
        self.j, self.i = pos.split(",")
        self.j = int(self.j)
        self.i = int(self.i)

    def __repr__(self) -> str:
        return f"({self.i}, {self.j})"


class Rock_segment():
    def __init__(self, pos: list[str]):
        self.points = []
        for a in range(len(pos)-1):
            self.points.append([Point2d(pos[a]), Point2d(pos[a+1])])

    def __repr__(self) -> str:
        msg = ""
        for i in range(len(self.points)):
            msg += self.points[i].__repr__() + ", "
        
        msg = msg[:-2]
        return msg


class Cave():
    def __init__(self, size_i: int, size_j: int, j_starts_at: int):
        self.size_i      = size_i
        self.size_j      = size_j
        self.j_starts_at = j_starts_at
        self.map         = ["."*self.size_j for _ in range(self.size_i)]

    def print(self) -> None:
        for line in self.map:
            print(line)

    @dispatch(list, str)
    def put(self, pos_list: list, char: str) -> None:
        for pos in pos_list:
            put(pos, char)


    @dispatch(Point2d, str)
    def put(self, pos: Point2d, char: str) -> None:
        """
        Puts in cave a point
        """

        j_index = pos.j - self.j_starts_at
        self.map[pos.i] = sub_in_string(self.map[pos.i], j_index, char)

    def put_segment(self, segment, char = "#") -> None:
        """
        Puts the segments of rock in cave
        """

        first_point  = None
        second_point = None

        for a in range(len(segment.points)):
            first_point  = segment.points[a][0]
            second_point = segment.points[a][1]  

            # --- Putting rocks in positions ---
            # Horizontal line
            if first_point.i == second_point.i:
                min_j = min(first_point.j, second_point.j)
                max_j = max(first_point.j, second_point.j)                
                for j in range(min_j, max_j+1):
                    self.put(Point2d(first_point.i, j), char)

            # Vertical line
            elif first_point.j == second_point.j:
                min_i = min(first_point.i, second_point.i)
                max_i = max(first_point.i, second_point.i)
                for i in range(min_i, max_i+1):
                    self.put(Point2d(i, first_point.j), char)
    
    def drop_sand(self, sand_pos: Point2d) :
        """
        Drops sand from position until it lands.
        Raises if fallen into abyss
        """
        sand_i = sand_pos.i
        sand_j = sand_pos.j - self.j_starts_at
        while True:
            sand_i += 1

            # Out of bounds
            abyss_msg = "Sand has fallen into abyss"
            if (sand_i + 1) >= len(self.map):           raise IndexError(abyss_msg)
            if sand_j < 0 or sand_j > len(self.map[0]): raise IndexError(abyss_msg)

            # Is air
            if self.map[sand_i+1][sand_j] == ".": continue

            # *** Is not air - colliding ***
            collide = {"#", "O"}

            # Bottom left
            if self.map[sand_i+1][sand_j-1] not in collide:
                sand_j -= 1
                continue
            # Bottom right
            if self.map[sand_i+1][sand_j+1] not in collide:
                sand_j += 1
                continue
            # Collides 
            self.map[sand_i] = sub_in_string(self.map[sand_i], sand_j, "O")
            return




def get_min_max(segments) -> dict:
    """
    Gets minimum and maximum values for segments
    """

    i_min, j_min = None, None
    i_max, j_max = None, None

    # Getting the minimum and maximum values for i and j
    for segment in segments:
        i_list, j_list = [], []

        for a in range(len(segment.points)):
            i_list.append(segment.points[a][0].i)
            i_list.append(segment.points[a][1].i)

            j_list.append(segment.points[a][0].j)
            j_list.append(segment.points[a][1].j)

        min_i_list, min_j_list = min(i_list), min(j_list)
        max_i_list, max_j_list = max(i_list), max(j_list)

        # Mininum i, j
        if i_min is None or j_min is None:
            i_min = min_i_list
            j_min = min_j_list
        else:
            i_min = min(min_i_list, i_min)
            j_min = min(min_j_list, j_min)

        # Maximum i, j
        if i_max is None or j_max is None:
            i_max = max_i_list
            j_max = max_j_list
        else:
            i_max = max(max_i_list, i_max)
            j_max = max(max_j_list, j_max)
    
    return {
        "i_min": i_min, 
        "j_min": j_min,  
        "i_max": i_max, 
        "j_max": j_max 
    }


def sub_in_string(string: str, index: int, change_to: str) -> str:
    """
    Returns a string with a value at index substituted to change_to char
    """

    return_string = string[:index] + change_to + (string[index+1:] if (index) < len(string) else "")
    return return_string


def main():
    with open("input.txt") as data:
        segments_base = data.read().splitlines()

    segments_base = [line.split(" -> ") for line in segments_base]
    segments = [Rock_segment(pos) for pos in segments_base]

    # Cave info
    min_max = get_min_max(segments)
    size_j = min_max["j_max"] - min_max["j_min"] + 1

    # cave = [["."*size_j] for i in range(min_max["i_max"]+1)]
    cave = Cave(min_max["i_max"]+1, size_j, min_max["j_min"])

    # Sand and rocks
    sand_pos = Point2d(0, 500)
    cave.put(sand_pos, "+")
    
    for segment in segments:
        cave.put_segment(segment)

    # Sand falling
    n_sand = 0
    while True:
        try:
            cave.drop_sand(sand_pos)
        except IndexError as e:
            break
        
        n_sand += 1

    cave.print()
    print(f'{n_sand} units of sand at the end')
    
    # Saving final graph to text file
    output_name = "graph.txt"
    print(f'Saving output to {output_name}')
    with open(output_name, "w") as f:
        for line in cave.map:
            f.write(line+'\n')


if __name__ == '__main__':
    main()