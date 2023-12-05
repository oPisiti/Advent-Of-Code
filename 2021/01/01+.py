def sum_three(list: list[int], init_i):
    return list[init_i] + list[init_i+1] + list[init_i+2]

def main():
    with open("input.txt") as data:
        depths = data.read().splitlines()
    
    depths = [int(depth) for depth in depths]

    larger_windows = 0
    window_A = sum_three(depths, 0)
    window_B =  int()
    for i in range(1, len(depths)-2):
        window_B = sum_three(depths, i)

        if window_B > window_A: larger_windows += 1
        window_A = window_B

    print(f"{larger_windows} larger windows")    


if __name__ == "__main__":
    main()