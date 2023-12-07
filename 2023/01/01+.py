"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import re


def sum_calibration_values(input: str = "input.txt") -> int:
    with open(input) as f:
        data = f.read().splitlines()

    numbers_list = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    sum_values = 0
    for line in data:
        sep = [0, 0]
        
        # Forward search
        sep0 = re.findall("\d|" + "|".join(numbers_list[1:]), line)[0]
        if len(sep0) > 0: sep[0] = sep0

        # Backwards search
        sep1 = re.findall("\d" + "|".join([num[::-1] for num in numbers_list]), line[::-1])[0]
        if len(sep1) > 0: sep[1] = sep1

        # Parsing and adding
        for i, s in enumerate(sep):
            try: 
                sep[i] = int(s)
            except ValueError as e:
                if i == 0:
                    sep[i] = numbers_list.index(s)
                else:
                    sep[i] = numbers_list.index(s[::-1])

        # Adding
        partial = 10 * sep[0] + sep[-1]

        sum_values += partial

        pass

    return sum_values


if __name__ == '__main__':
    print(sum_calibration_values())
