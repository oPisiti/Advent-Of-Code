def count_0s(rep: list[str]) -> str:
    count_0 = [0 for i in range(len(rep[0]))]

    # Counting the number of 0 bits in order
    for num in rep:
        for i, bit in enumerate(num):
            if bit == "0": count_0[i] += 1

    return count_0

def get_rating(report: list[str], most_common = True) -> str:
    temp_report = report.copy()
    temp_gen_rating = ""
    analyse_bit = 0

    while len(temp_report) > 1:
        temp_count_0 = count_0s(temp_report)

        if most_common:
            must_equal = "0" if temp_count_0[analyse_bit] > (len(temp_report)/2) else "1"
        else:
            must_equal = "1" if temp_count_0[analyse_bit] > (len(temp_report)/2) else "0"

        temp_report = [rep for rep in temp_report if rep[analyse_bit] == must_equal]
        analyse_bit += 1

    return temp_report[0]


def get_power_consumption():
    with open("input.txt") as data:
        report = data.read().splitlines()

    o_generator_rating = get_rating(report)
    print(f"o_generator_rating:  {o_generator_rating}")

    c02_scrubber_rating = get_rating(report, most_common=False)
    print(f"c02_scrubber_rating: {c02_scrubber_rating}")

    # Defining the power consumption
    o_generator_rating   = int(o_generator_rating,  base=2)
    c02_scrubber_rating  = int(c02_scrubber_rating, base=2)
    print(f"life support rating: {o_generator_rating * c02_scrubber_rating} units")


if __name__ == '__main__':
    get_power_consumption()