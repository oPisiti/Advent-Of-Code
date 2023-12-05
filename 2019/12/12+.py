import re
from moon import *

def main():
    # Variables
    n_steps    = 1000
    show_steps = False

    with open("input.txt") as data:
        inp = data.read().splitlines()
    
    moons = []
    for line in inp:
        moons.append(Moon([int(a) for a in re.findall("=(-*\d+)", line)]))

    # Iterations
    steps = 0
    if show_steps: 
        print(f"After {steps} steps:")
        for moon in moons:
            print(moon)
    
    for _ in range(n_steps):
        apply_gravity_all(moons)
        steps += 1
        if show_steps:
            print(f"\nAfter {steps} steps:")
            for moon in moons:
                print(moon)

    # Energy
    total_energy = get_total_energy(moons)
    print(f'\nTotal energy after {steps}: {total_energy} units')


if __name__ == '__main__':
    main()