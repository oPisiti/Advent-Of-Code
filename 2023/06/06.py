from math import sqrt, ceil, floor
import re

def races():
    with open("input.txt") as f:
        data = f.read()

    times, dists = re.findall("\w+: +((\d+ *)+)", data)
    times = [int(n) for n in re.split(" +", times[0])]
    dists = [int(n) for n in re.split(" +", dists[0])]
    
    answer = 1

    # Solving parabolic equation
    for i, time in enumerate(times):
        sqr_delta = sqrt(time**2 - 4*dists[i])
        tmin = (time - sqr_delta) / 2
        tmax = (time + sqr_delta) / 2

        ways_count = ceil(tmax) - floor(tmin) - 1
        answer *= ways_count

    return answer


if __name__ == '__main__':
    print(races())