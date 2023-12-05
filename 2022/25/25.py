def SNAFU2dec(num: str) -> int:
    res = 0
    power = 1
    for i in range(len(num)-1, -1, -1):
        digit = 0

        match num[i]:
            case "=": digit = -2
            case "-": digit = -1
            case _:   digit = int(num[i])

        res += digit * power
        power *= 5
    
    return res

def dec2SNAFU(num: int) -> str:
    res = ""

    # Getting closest biggest number
    



def sum_numbers():
    with open("input.txt") as data:
        numbers_SNAFU = data.read().splitlines()

    # Translating all numbers to decimal
    numbers_dec = [SNAFU2dec(num) for num in numbers_SNAFU]

    print(numbers_dec)

if __name__ == '__main__':
    sum_numbers()