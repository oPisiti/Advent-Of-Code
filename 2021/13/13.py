import re
import numpy as np

def print_list_nicely(li: list) -> None:
    for row in li:
        print(row)


def apply_fold(dots: list[str], fold: list[str]) -> list[str]:
    # is_even = not len(dots)%2

    match fold[0]:
        case "x":
            j_max = int(len(dots[0])/2) 

            for i in range(len(dots)):
                dots[i] = overlap(dots[i], dots[i][::-1])
                dots[i] = dots[i][:j_max]            

        case "y":
            i_max = int(len(dots)/2)

            for i in range(i_max):
                dots[i] = overlap(dots[i], dots[len(dots)-1-i])
            
            dots = dots[:i_max] 

        case _:
            msg = f"Folding along {fold[0]} not supported"
            raise NotImplementedError(msg)

    return dots


def overlap(string: str, overlapper: str) -> str:
    """
    Overlaps two strings and returns 'string'.
    Char # is prioritized
    """
    # print(f"string:    {string}")
    # print(f"overlaper: {overlapper}")

    for j in range(len(string)):
        if string[j] == "." and overlapper[j] == "#":
            string = string[:j] + "#" + (string[j+1:] if (j+1)<len(string) else "")

    return string


def count_dots(dots_list: list[str]) -> int:
    count = 0
    for row in dots_list:
        for item in row:
            if item == "#": count += 1

    return count


def main():
    # Dealing with input
    with open("input.txt") as data:
        dots_list, instructions = data.read().split("\n\n")
    
    dots_list = dots_list.split("\n")
    dots_list = [a.split(",") for a in dots_list]
    dots_list = [list(map(int, i)) for i in dots_list]
    # print(dots_list)

    instructions = re.findall("\w=\d", instructions)
    instructions = [inst.split("=") for inst in instructions]
    print(instructions)

    i_max = max([i for [i, j] in dots_list]) + 1
    j_max = max([j for [i, j] in dots_list]) + 1
    dots = ["."*i_max for i in range(j_max)]
    
    for point in dots_list:
        dots[point[1]] = dots[point[1]][:point[0]] + "#" + (dots[point[1]][point[0]+1:] if j_max > (point[0]+1) else "")

    # Folding
    have_folded = 0
    for fold in instructions:
        dots = apply_fold(dots, fold)
        have_folded += 1
        print(f"Fold {have_folded}: there are {count_dots(dots)} dots")
        # print_list_nicely(dots)
        
        



if __name__ == '__main__':
    main()