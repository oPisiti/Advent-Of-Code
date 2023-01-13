import re
import numpy as np

def apply_flash(levels: np.array, i_: int, j_: int, has_flashed_indexes: list[int]):
    """
    Applies flash to a specific octupus and increases its 
    surroundings levels by 1. Disconsiders already flashes ones
    """
    
    levels[i_][j_] = 0            
    i_max, j_max   = levels.shape

    # Increasing surrounding octopuses' levels by 1
    for i in range(i_-1, i_+2):
        for j in range(j_-1, j_+2):
            if i == i_ and j == j_:           continue
            if i < 0 or j < 0:                continue
            if i >= i_max or j >= j_max:      continue
            if [i, j] in has_flashed_indexes: continue

            levels[i][j] += 1


def apply_iteration(levels: np.array) -> int:
    """
    Applies one iteration over all octopuses.
    Returns the amount of flashes in this iteration
    """

    has_flashed_indexes = []
    levels += 1

    sum_flashes_iteration = 0
    while levels.max() > 9:
        i_max, j_max = levels.shape
        for i in range(i_max):
            for j in range(j_max):
                if levels[i][j] > 9: 
                    apply_flash(levels, i, j, has_flashed_indexes)
                    sum_flashes_iteration += 1
                    
                    if [i, j] not in has_flashed_indexes: 
                        has_flashed_indexes.append([i, j])
    
    return sum_flashes_iteration


def main():
    with open("input.txt") as data:
        energy_levels_base = data.read().splitlines()
    
    energy_levels_base = [re.findall("\d{1}", line) for line in energy_levels_base]
    energy_levels      = np.array(energy_levels_base, dtype=np.uint8)

    # Iterations
    n_iterations    = 0
    sum_flashes_all = 0
    while np.count_nonzero(energy_levels) != 0:
        sum_flashes_all += apply_iteration(energy_levels)
        n_iterations += 1

    print(f"There were {n_iterations} iterations before syncronization")


if __name__ == '__main__':
    main()