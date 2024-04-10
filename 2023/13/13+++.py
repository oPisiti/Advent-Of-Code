"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""


def get_vertical(mirror: list[str], index: int) -> str:
    return "".join([s[index] for s in mirror])


def mirrors():
    with open("input.txt") as f:
        data = [m.split("\n") for m in f.read().strip().split("\n\n")]
    
    # Creating the hashes for every row and column
    mirrors_horizontal = []
    mirrors_vertical   = []
    for mirror in data:
        mirrors_horizontal.append(mirror)
        mirrors_vertical.append([get_vertical(mirror, index) for index in range(len(mirror[0]))])

    # Finding the one-smudge-away pair of lines 
    h_smudge = []
    for i in range(len(mirrors_horizontal)):
        found_smudge = False
        
        # Horizontal
        found_smudge = fix_smudge(mirrors_horizontal[i], mirrors_vertical[i])

        if found_smudge: h_smudge.append(True)
        
        # Vertical
        else:
            found_smudge = fix_smudge(mirrors_vertical[i], mirrors_horizontal[i])
            h_smudge.append(False)

    # Calculating the answers
    answer = 0
    for i in range(len(mirrors_horizontal)):
        mirror = mirrors_horizontal[i] if h_smudge[i] else  mirrors_vertical[i]

        l, r = 0, 1
        while 0 <= l < len(mirror) and 0 <= r < len(mirror):
            
            # Is the middle
            if mirror[l] == mirror[r] and check_middle(mirror, l, r): 
                
                # Score based on the type of reflection
                if h_smudge[i]: answer += 100 * r
                else:           answer += r

                break

            l = r
            r += 1

    return answer


def fix_smudge(main: list[str], sec: list[str]) -> bool:
    smudge_found = False

    # Looping through every pair
    for i in range(len(main)):
        for j in range(i+1, len(main)):
            diff = 0

            # Searching for a smudge
            first_diff = 0
            for c in range(len(main[0])):
                if main[i][c] != main[j][c]:
                    diff += 1
                    if diff > 1: break
                    first_diff = c

            # Fixing the one-smudge-away pair of lines
            if diff == 1:
                main[i] = main[i][:first_diff] + main[j][first_diff] + main[i][first_diff+1:]
                sec[first_diff] = sec[first_diff][:i] + sec[first_diff][j] + sec[first_diff][i+1:]

                smudge_found = True
                break
        
        if smudge_found: break
    
    return smudge_found


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