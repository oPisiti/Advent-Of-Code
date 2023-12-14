"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""


def get_vertical_hash(mirror: list[str], index: int) -> int:
    return hash("".join([s[index] for s in mirror]))



def mirrors():
    with open("input.txt") as f:
        data = [m.split("\n") for m in f.read().strip().split("\n\n")]
    
    # Creating the hashes for every row and column
    mirrors_horizontal = []
    mirrors_vertical   = []
    for mirror in data:
        mirrors_horizontal.append(tuple(hash(m) for m in mirror))
        mirrors_vertical.append(tuple(get_vertical_hash(mirror, index) for index in range(len(mirror[0]))))

    # Calculating the answers
    answer = 0
    for i in range(len(mirrors_horizontal)):
        horizontal = True
        for mirror in [mirrors_horizontal[i], mirrors_vertical[i]]:
            l, r = 0, 1

            while l >= 0 and l < len(mirror) and r >= 0 and r < len(mirror):
                
                # Is the middle
                if mirror[l] == mirror[r] and check_middle(mirror, l, r): 
                    
                    # Score based on the type of reflection
                    if horizontal: 
                        answer += 100 * r
                    else:              
                        answer += r

                l = r
                r += 1
            
            horizontal = False

    pass

    return answer


def check_middle(mirror: list[int], l: int, r: int) -> bool:
    i_l, i_r = l, r

    while i_l >= 0 and i_r < len(mirror):
        if mirror[i_l] != mirror[i_r]:
            return False

        i_l -= 1
        i_r += 1

    return True


if __name__ == '__main__':
    print(mirrors())