import numpy as np
import re


def lowest_location_number() -> int:
    with open("input.txt") as f:
        data = f.read().strip().split("\n\n")
    
    # Seeds values
    base_seeds = tuple(int(s) for s in re.search("seeds: ((\d+ ?)+)", data[0]).groups()[0].split(" "))
    
    

    ## Seeds are actually given in the form of ranges
    # seeds = []
    # for i in range(0, len(base_seeds), 2):
    #     seeds += [i for i in range(base_seeds[i], base_seeds[i] + base_seeds[i+1])]

    # Mappings - Parsing
    mappings = []
    for i in range(1, len(data)):
        mappings.append(tuple(tuple(int(s_m) for s_m in m.split(" ")) for m in data[i].split("\n")[1:]))

    # Sorted ranges with smallest location
    location_ranges_ordered = sorted(mappings[-1], key=lambda x: x[0])
    

    # The following algorithm first determines which location range is reachable
    # It start by the lowest location range and applies inverse steps until it reaches the seeds
    # When it hits a seed range, it goes back and tries all possibilities
    
    # Outer loop
    for loc_range in location_ranges_ordered:
        # Inverse level relative to mappings. Level -1 means seeds and 6 (len(mappings) - 1), locations
        level = len(mappings) - 1

        # curr_range is formatted as [destination, length]
        curr_range = [[loc_range[0], loc_range[2]],]
        
        while level >= 0 and curr_range is not None:
            # curr_range = up_level(mappings, curr_range, level)

            level -= 1

        # Reached the seeds level
        if curr_range is not None: break

    # Loop ended with no valid results
    if curr_range is None: return f"Unable to reach the seeds level"

    # Loop ended after reaching a seeds ranges
    # TODO: Finding the best seed


    pass
    

def up_level(mappings: list[tuple[tuple]], curr_range: list[list], level: int) -> list[list]:
    output_range = []
    
    while len(curr_range) > 0:
        # Each separate range will be reduced, one at a time
        for r in curr_range:
            # Finding the start position at the level
            start_position_range = find_start_position(mappings[level], r[0])


    return output_range


def find_start_position(mapping: tuple[tuple], ran: list) -> list:
    for range_pos in mapping:
        if ran[0] range_pos[0]



if __name__ == '__main__':
    print(lowest_location_number())