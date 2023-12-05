from multipledispatch import dispatch

class Point3D():
    @dispatch(int, int, int)
    def __init__(self, _x: int, _y: int, _z: int):
        self.x = _x
        self.y = _y
        self.z = _z

    @dispatch(list)
    def __init__(self, pos: list[str]):
        self.__init__(int(pos[0]), int(pos[1]), int(pos[2]))


def count_collisions(index: int, cubes: list[Point3D]):
    count = 0
    for i in range(len(cubes)):
        if i == index: continue
        diff = [abs(cubes[i].x-cubes[index].x),
                abs(cubes[i].y-cubes[index].y),
                abs(cubes[i].z-cubes[index].z)]
        
        if diff.count(0) == 2 and diff.count(1) == 1:
            count += 1

    return count


def main():
    with open("input.txt") as data:
        cubes = data.read().splitlines()

    cubes = [Point3D(cube.split(",")) for cube in cubes]

    n_col = 0
    for index_cube in range(len(cubes)):
        n_col += count_collisions(index_cube, cubes)

    total_area = 6*len(cubes) - n_col
    print(f"Total area: {total_area}")
    

if __name__ == "__main__":
    main()