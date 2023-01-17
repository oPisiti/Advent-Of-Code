def req_fuel(mass: int) -> int:
    return int(mass/3) - 2


def main():
    with open("input.txt") as data:
        masses = data.read().splitlines()

    masses = [int(mass) for mass in masses]

    sum_fuel = 0
    for mass in masses:
        partial_fuel = req_fuel(mass)
        
        while partial_fuel > 0:
            sum_fuel += partial_fuel
            partial_fuel = req_fuel(partial_fuel)

    print(f'Total fuel requirement: {sum_fuel}')


if __name__ == '__main__':
    main()