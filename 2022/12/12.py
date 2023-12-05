def findS(h, letter):
    for i in range(len(h)):
        for j in range(len(h[i])):
            if h[i][j] == letter: return {"i":i, "j":j}

def main():
    with open("input.txt") as data:
        heights = data.read().split("\n")

    S = findLetter(heights, "S")
    
    # Possible moves
    possible =

    for line in heights: print(line)


if __name__ == '__main__':
    main()