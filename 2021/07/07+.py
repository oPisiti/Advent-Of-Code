from timeMe import timeMe

def sum_down(a: int) -> int:
    my_sum = 0
    for i in range(a+1): my_sum += i

    return my_sum


def get_fuel(pos: dict, a: int) -> int:
    fuel = 0
    for item in pos:
        fuel += sum_down(abs(item - a)) * pos[item]

    return fuel


@timeMe
def main():
    with open("input.txt") as data:
        pos = data.read().split(",")

    # Counting appearances into a dictionary
    pos_dict = {}
    for item in pos:
        item = int(item)
        if item in pos_dict: pos_dict[item] += 1
        else:                pos_dict[item] =  1

    # print(f"pos_dict: {pos_dict}")

    # Calculating all fuel consumptions until it starts to rise (local/global minimum)
    fuel_list = []
    for i in range(min(pos_dict.keys()), max(pos_dict.keys())):
        latest_fuel_count = get_fuel(pos_dict, i)
        if len(fuel_list) == 0 or latest_fuel_count < fuel_list[-1]:
            fuel_list.append(latest_fuel_count)

    # print(f"Fuel list: {fuel_list}")
    print(f"Smallest amount of consumed fuel: {min(fuel_list)}")


if __name__ == '__main__':
    main()