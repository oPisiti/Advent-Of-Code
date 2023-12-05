def get_power_consumption():
    with open("input.txt") as data:
        report = data.read().splitlines()

    count_0 = [0 for i in range(len(report[0]))]

    # Counting the number of 0 bits in order
    for num in report:
        for i, bit in enumerate(num):
            if bit == "0": count_0[i] += 1
    
    # Defining the gamma rate
    gamma_rate = ""
    for count in count_0:
        if count > (len(report)/2): gamma_rate = gamma_rate + "0"
        else:                       gamma_rate = gamma_rate + "1" 

    # defining the epsilon rate by switching the bits in the gamma rate
    epsilon_rate = ""
    for bit in gamma_rate:
        if bit == "1":              epsilon_rate = epsilon_rate + "0"
        else:                       epsilon_rate = epsilon_rate + "1"

    # Defining the power consumption
    gamma_rate_decimal   = int(gamma_rate,   base=2)
    epsilon_rate_decimal = int(epsilon_rate, base=2)
    print(f"Power consumption: {gamma_rate_decimal * epsilon_rate_decimal} units")


if __name__ == '__main__':
    get_power_consumption()