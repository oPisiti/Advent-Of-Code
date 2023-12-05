def Conway():
    currentBoard = 1
    boards = [["."*8 for i in range(8)]]

    with open("input.txt") as data:
        boards.append(data.read().split("\n"))

    print(boards)


if __name__ == '__main__':
    Conway()