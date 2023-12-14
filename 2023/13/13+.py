"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

def mirrors():
    with open("input.txt") as f:
        data = [m.split("\n") for m in f.read().strip().split("\n\n")]
    
    # Calculating the answers
    answer = 0
    for i, mirror in enumerate(data):
        horizontal = True

        for _ in range(2):
            # Symmetries
            l, r = 0, 1
            while l < len(mirror) and r < len(mirror):
                
                # Is the middle
                if mirror[l] == mirror[r]:                
                    if diff_is_one(mirror, l, r, horizontal): 

                        # Score based on the type of reflection
                        if horizontal: 
                            answer += 100 * r
                            print(f"h: {r}")
                        else:              
                            answer += r
                            print(f"v: {r}")

                l = r
                r += 1

            horizontal = False

    pass

    return answer


def diff_is_one(mirror: list[int], l: int, r: int, horizontal: bool) -> bool:
    i_l, i_r = l, r

    max_i = len(mirror) if horizontal else len(mirror[0])

    for i_l in range(max_i):
        for i_r in range(i_l + 1, max_i):
            if horizontal:
                if mirror[i_l] != mirror[i_r]:
                    # Calculating the difference in strings
                    diff = 0
                    for k in range(len(mirror[i_l])):
                        if mirror[i_l][k] != mirror[i_r][k]:
                            diff += 1
                    
                    if diff == 1: return True
                    return False
            
            else:
                v_l_str = "".join([s[i_l] for s in mirror])
                v_r_str = "".join([s[i_r] for s in mirror])
                if v_l_str != v_r_str:
                    # Calculating the difference in strings
                    diff = 0
                    for k in range(len(v_l_str)):
                        if v_l_str[k] != v_r_str[k]:
                            diff += 1
                    
                    if diff == 1: return True
                    return False
    
    return False


    # while i_l >= 0 and i_r < max_i:
    #     if horizontal:

    #         if mirror[i_l] != mirror[i_r]:
    #             # Calculating the difference in strings
    #             diff = 0
    #             for k in range(len(mirror[i_l])):
    #                 if mirror[i_l][k] != mirror[i_r][k]:
    #                     diff += 1
                
    #             if diff == 1: return True
    #             return False
        
    #     else:
    #         v_l_str = "".join([s[i_l] for s in mirror])
    #         v_r_str = "".join([s[i_r] for s in mirror])
    #         if v_l_str != v_r_str:
    #             # Calculating the difference in strings
    #             diff = 0
    #             for k in range(len(v_l_str)):
    #                 if v_l_str[k] != v_r_str[k]:
    #                     diff += 1
                
    #             if diff == 1: return True
    #             return False

    #     i_l -= 1
    #     i_r += 1
    
    # return False


if __name__ == '__main__':
    print(mirrors())