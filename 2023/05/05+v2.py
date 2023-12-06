import numpy as np
import re


def lowest_location_number() -> int:
    with open("input.txt") as f:
        data = f.read().strip().split("\n\n")
    
    # Seeds values
    base_seeds = tuple(int(s) for s in re.search("seeds: ((\d+ ?)+)", data[0]).groups()[0].split(" "))

    # Mappings - Parsing
    mappings = []
    for i in range(1, len(data)):
        mappings.append(tuple(tuple(int(s_m) for s_m in m.split(" ")) for m in data[i].split("\n")[1:]))

    # Sorted ranges with smallest location
    location_ranges_ordered = sorted(mappings[-1], key=lambda x: x[0])

    # Calculating the seed for each location number
    for loc in range(10_000_000):
        if not loc%1_000_000: print(loc)
        seed = get_seed(mappings, loc)
        
        # Valid seed
        for i in range(0, len(base_seeds), 2):
            if seed >= base_seeds[i] and seed < (base_seeds[i] + base_seeds[i+1]):
                return loc

    # No valid path
    return None


def get_seed(mappings: tuple[tuple], location: int) -> int:
    curr = location

    # Inverse travel 
    for i in range(len(mappings)-1, -1, -1):
        for rule in mappings[i]:
            # Found the next range
            if curr >= rule[0] and curr < (rule[0] + rule[2]):
                curr = curr - rule[0] + rule[1]
                break        
                
    # Found all ranges
    return curr               


if __name__ == '__main__':
    print(lowest_location_number())