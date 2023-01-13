def main():
    with open("input.txt") as data:
        depths = data.read().splitlines()

    depths = [int(measure) for measure in depths]

    larger_measurements = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]: larger_measurements += 1

    print(f"{larger_measurements} larger measurements")


if __name__ == '__main__':
    main()