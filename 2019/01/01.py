def main():
    with open("input.txt") as data:
        masses = data.read().splitlines()

    masses = [int(mass) for mass in masses]

    sum_fuel = 0
    for mass in masses:
        sum_fuel += int(mass/3) - 2
    
    print(f'Total fuel requirement: {sum_fuel}')


if __name__ == '__main__':
    main()