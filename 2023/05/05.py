import numpy as np
import re


def lowest_location_number() -> int:
    with open("input.txt") as f:
        data = f.read().strip().split("\n\n")
    
    # Seeds values
    seeds = tuple(int(s) for s in re.search("seeds: ((\d+ ?)+)", data[0]).groups()[0].split(" "))
    
    # Mappings - Parsing
    mappings = []
    for i in range(1, len(data)):
        mappings.append(tuple(tuple(int(s_m) for s_m in m.split(" ")) for m in data[i].split("\n")[1:]))

    # Calculating the lowest location number
    lowest_location = np.inf
    for seed in seeds:
        curr_loc = get_location(mappings, seed)
        if curr_loc < lowest_location:
            lowest_location = curr_loc

    return lowest_location


def get_location(mappings: tuple[tuple], seed: int) -> int:
    source = seed
    destination = None

    for mapper in mappings:
        for rule in mapper:
            # Found the range
            if source >= rule[1] and source < (rule[1] + rule[2]):
                destination = source - rule[1] +rule[0]
                source = destination
                break
                

    return destination               


if __name__ == '__main__':
    print(lowest_location_number())