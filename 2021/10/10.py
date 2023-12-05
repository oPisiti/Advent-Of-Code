def check_char(opened_chars: list[str], char: str) -> None:
    """
    Checks if char is the expected character
    """
    opening = "([{<"
    closing = ")]}>"

    try:
        # Char is opening character
        char_in_opening_index = opening.index(char)
        opened_chars.append(char)
    except ValueError as e:
        # Char is closing character
        expected_closing = closing[opening.index(opened_chars[-1])]
        
        if char != expected_closing:                    
            error_msg = f"Expected {expected_closing} and found {char}"
            raise ValueError(error_msg) from e

        opened_chars = opened_chars.pop(-1)


def update_syntax_score(score: int, char: str) -> int:
    points={
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    score += points[char]

    return score


def main():
    with open("input.txt") as data:
        subsystem_base = data.read().splitlines()
    
    # print(subsystem_base)
    syntax_score = 0
    for line in subsystem_base:
        if line[0] in "([{<": expected = []
        else:                 raise ValueError(f"First char in {line} is not an opening char")
        
        for char in line:
            try:
                check_char(expected, char)
            except ValueError as e:
                syntax_score = update_syntax_score(syntax_score, char)
                break

    print(f"Total syntax error score: {syntax_score}")


if __name__ == '__main__':
    main()