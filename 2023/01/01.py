"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import re


def sum_calibration_values(input: str = "input.txt") -> int:
    with open(input) as f:
        data = f.read().splitlines()

    sum_values = 0

    for line in data:

        digits = re.findall("\d", line)

        sum_values += 10 * int(digits[0]) + int(digits[-1])

    return sum_values


if __name__ == '__main__':
    print(sum_calibration_values())
