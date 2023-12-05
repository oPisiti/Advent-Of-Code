def gen_completion_string(string: str) -> str:
    """
    Generates a string that correctly completes a string, given the following\
    sequences
    """
    opening = "([{<"
    closing = ")]}>"

    opened_chars = ""
    for char in string: 
        try:
            # Char is opening character
            char_in_opening_index = opening.index(char)
            opened_chars += char
        except ValueError as e:
            # Char is closing character
            expected_closing = closing[opening.index(opened_chars[-1])]
            
            # String is corrupted
            if char != expected_closing:                 
                error_msg = f"Expected {expected_closing} and found {char}"
                raise ValueError(error_msg) from e

            opened_chars = opened_chars[:-1]
    

    return get_closing_char_from_opening(opened_chars, opening, closing)


def get_closing_char_from_opening(opening_chars: str, accepted_opening_chars: str, accepted_closing_chars: str) -> str:
    """
    Returns a string that correctly completes a string, given its asjusted opening chars sequence
    """

    closing_chars = ""
    for i in range(len(opening_chars)-1, -1, -1):
        opening_index = accepted_opening_chars.index(opening_chars[i])
        closing_chars += accepted_closing_chars[opening_index]
    
    return closing_chars


def get_syntax_score(string: str) -> int:
    points={
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    score = 0
    for char in string:
        score *= 5
        score += points[char]

    return score


def main():
    with open("input.txt") as data:
        subsystem_base = data.read().splitlines()
    
    # Getting a list of indexes of the corrupted lines
    completion_string = []
    for i, line in enumerate(subsystem_base):
        if line[0] in "([{<": expected = ""
        else:                 raise ValueError(f"First char in {line} is not an opening char")

        try:
            completion_string.append(gen_completion_string(line))
        except ValueError as e:
            continue

    # Getting score
    syntax_score = []
    for line in completion_string:
        syntax_score.append(get_syntax_score(line))
    
    syntax_score.sort()
    winner_score = syntax_score[int(len(syntax_score)/2)]
    print(f"Middle score: {winner_score}")


if __name__ == '__main__':
    main()