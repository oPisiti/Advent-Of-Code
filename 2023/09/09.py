"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""


def prediction() -> int:
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    
    histories = [[int(number) for number in d.split(" ")] for d in data]

    answer = 0

    for i in range(len(histories)):
        size = len(histories[i])

        # Reaching 0
        while not all_zeroes(histories[i], size):
            for j in range(size-1):
                histories[i][j] = histories[i][j+1] - histories[i][j]

            size -= 1

        # Calculating the prediction
        answer += sum(histories[i])
        pass

    return answer

def all_zeroes(history: list[int], size_to_check: int) -> bool:
    for i in range(size_to_check):
        if history[i] != 0: return False

    return True


if __name__ == '__main__':
    print(prediction())