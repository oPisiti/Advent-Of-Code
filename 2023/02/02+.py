from functools import reduce
import re


def possible_games() -> int:
    with open("input.txt") as f:
        data = f.readlines()

    sum_powers = 0

    games = []
    for game in data:
        g = game.split(":")[1].rstrip("\n").split(";")
        games.append([partial.strip() for partial in g])

    for i, game in enumerate(games):
        fewest_number = get_fewest_number(game)
        power = reduce(lambda x, y: x*y, [v for v in fewest_number.values()])
        sum_powers += power

    return sum_powers


def get_fewest_number(game: list) -> dict:

    fewest_counts = {
        "red":   0,
        "green": 0,
        "blue":  0
    }
    
    for handful in game:
        tokens = re.findall("\d+|\w+", handful)
        
        for j in range(0, len(tokens), 2):
            if int(tokens[j]) > fewest_counts[tokens[j+1]]:
                fewest_counts[tokens[j+1]] = int(tokens[j])
        
    return fewest_counts
    

if __name__ == '__main__':
    print(possible_games())