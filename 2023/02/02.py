import re


def possible_games() -> int:
    with open("input.txt") as f:
        data = f.readlines()
    
    game_max_count = {
            "red":   12,
            "green": 13,
            "blue":  14
    }

    answer = 0

    games = []
    for game in data:
        g = game.split(":")[1].rstrip("\n").split(";")
        games.append([partial.strip() for partial in g])

    for i, game in enumerate(games):
        if is_game_valid(game, game_max_count): 
            answer += int(i+1)

    return answer


def is_game_valid(game: list, game_max_count: dict) -> bool:
    for handful in game:
        dice_counts = {
            "red":   0,
            "green": 0,
            "blue":  0
        }

        tokens = re.findall("\d+|\w+", handful)
        for j in range(0, len(tokens), 2):
            dice_counts[tokens[j+1]] = int(tokens[j])
        
        # Determining if game is possible
        for key, value in dice_counts.items():
            # Invalid hand
            if game_max_count[key] < int(value): 
                return False
    
    return True


if __name__ == '__main__':
    print(possible_games())