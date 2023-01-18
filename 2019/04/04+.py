def cout_valid(start: str, end: str) -> str:
    """
    Count valid numbers between start and end based on:
    (1) It is a six-digit number.
    (2) The value is within the range given in your puzzle input.
    (3) Two adjacent digits are the same (like 22 in 122345).
    (4) Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

    Returns 0 if False, 1 if True
    """

    int_start, int_end = int(start), int(end)

    for i in range(int_start, int_end + 1):
        checks = {
            "good_length"   : True,
            "double_digits" : False,
            "increase_only" : True}

        num = str(i)

        if len(num) != 6: checks["good_length"]  = False    # (1)

        count_digits = {}
        for dig in num:                                     # (3)
            count = num.count(str(dig))
            if dig not in count_digits.keys(): count_digits[dig] =  1
            else:                              count_digits[dig] += 1     

        if 2 in count_digits.values():         checks["double_digits"] = True


        for i in range(len(num) - 1):
            if checks["increase_only"] and num[i] > num[i + 1]: # (4)
                checks["increase_only"] = False

        if all(check for check in checks.values()): yield 1
        else:                                       yield 0 


def main():
    lower, upper = "156218", "652527"
    nums = cout_valid(lower, upper)

    n_valid = 0
    for num in nums:
        n_valid += num

    print(f"Number of valid digits: {n_valid}")


if __name__ == "__main__":
    main()
