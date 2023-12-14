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
    all_hashes_hor = []
    all_hashes_vert   = []
    for mirror in data:
        all_hashes_hor.append([hash(m) for m in mirror])
        all_hashes_vert.append([get_vertical_hash(mirror, index) for index in range(len(mirror[0]))])

    # Attempting to change a smudge
    score = 0
    for p, pattern in enumerate(data):
        score += find_new_line(pattern, all_hashes_hor[p], all_hashes_vert[p])
        
    return score


def check_middle(mirror: list[int], l: int, r: int) -> bool:
    i_l, i_r = l, r

    while i_l >= 0 and i_r < len(mirror):
        if mirror[i_l] != mirror[i_r]:
            return False

        i_l -= 1
        i_r += 1

    return True


def find_new_line(pattern: list[str], hashes_hor: list[int], hashes_vert: list[int]) -> int:
    base_score = get_score(hashes_hor, hashes_vert)

    base_i, base_j = get_min_sym(hashes_hor), get_min_sym(hashes_vert)

    for i, pattern_line in enumerate(pattern):
        original_line = pattern[i]
        for j, _ in enumerate(pattern_line):
            # Updating the string
            new_char = "#" if pattern[i][j] == "." else "."
            pattern[i] = original_line[:j] + new_char
            
            try:
                pattern[i] += original_line[j+1:]
            except IndexError as e:
                pass

            # Updating the hashes lists
            hashes_hor[i]  = hash(pattern[i])
            hashes_vert[j] = get_vertical_hash(pattern, j)
            
            # Scores    
            curr_i, curr_j = get_min_sym(hashes_hor), get_min_sym(hashes_vert)
            if curr_i < base_i:
                curr_score = get_score(hashes_hor, [])
                return curr_score
            if curr_j < base_j:
                curr_score = get_score([], hashes_vert)
                return curr_score

            # Resetting line to original value
            pattern[i] = original_line
    
    return base_score


def get_min_sym(mirror: list[int]) -> int:

    l, r = 0, 1

    while l >= 0 and r < len(mirror):
        
        # Is the middle
        if mirror[l] == mirror[r] and check_middle(mirror, l, r): 
            
            i_l, i_r = l, r

            while i_l >= 0 and i_r < len(mirror):
                if mirror[i_l] != mirror[i_r]:
                    return i_l + 1

                i_l -= 1
                i_r += 1

            return i_l + 1

        l = r
        r += 1

    return l + 1


def get_score(hashes_hor: list[int], hashes_vert: list[int]) -> int:
    score = 0

    horizontal = True
    for mirror in [hashes_hor, hashes_vert]:
        l, r = 0, 1

        while l >= 0 and l < len(mirror) and r >= 0 and r < len(mirror):
            
            # Is the middle
            if mirror[l] == mirror[r] and check_middle(mirror, l, r): 
                
                # Score based on the type of reflection
                if horizontal: 
                    score += 100 * r
                else:              
                    score += r
                break

            l = r
            r += 1
        
        horizontal = False
    
    return score


def get_lines(hashes_hor: list[int], hashes_vert: list[int]) -> (int, int):
    h_value, v_value = None, None

    horizontal = True
    for mirror in [hashes_hor, hashes_vert]:
        l, r = 0, 1

        while l >= 0 and l < len(mirror) and r >= 0 and r < len(mirror):
            
            # Is the middle
            if mirror[l] == mirror[r] and check_middle(mirror, l, r): 
                if horizontal: h_value = r
                else:          v_value = r

            l = r
            r += 1
        
        horizontal = False
    
    return h_value, v_value


if __name__ == '__main__':
    print(mirrors())