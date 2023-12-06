from math import sqrt, ceil, floor
import re

def races():
    with open("input.txt") as f:
        data = f.read().split("\n")

    time = re.findall("\d+", data[0])
    dist = re.findall("\d+", data[1])

    time = int("".join(time))
    dist = int("".join(dist))
    
    # Solving parabolic equation
    sqr_delta = sqrt(time**2 - 4*dist)
    tmin = (time - sqr_delta) / 2
    tmax = (time + sqr_delta) / 2

    ways_count = ceil(tmax) - floor(tmin) - 1

    return ways_count


if __name__ == '__main__':
    print(races())