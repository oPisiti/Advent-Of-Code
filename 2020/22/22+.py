import re

def main():
    with open("input.txt") as data:
        decks= data.read().split("\n\n")

    [deck1, deck2] = [[int(a) for a in re.findall("\d+", deck)[1:]] for deck in decks]

    rounds = 0
    while len(deck1) and len(deck2):
        # print(f"Deck1: {deck1}")
        # print(f"Deck2: {deck2}")
        # print(f"Comparing {deck1[0]} with {deck2[0]}")
        if deck1[0] > deck2[0]:
            deck1.append(deck1[0])
            deck1.append(deck2[0])
            deck1.pop(0)
            deck2.pop(0)
        else:
            deck2.append(deck2[0])
            deck2.append(deck1[0])
            deck1.pop(0) 
            deck2.pop(0)

        rounds += 1

    # print(f"After {rounds} rounds:")
    # print(f"Deck1: {deck1}")
    # print(f"Deck2: {deck2}")

    # Calculating the final winner's score
    winnerDeck = deck1 if len(deck1) > 0 else deck2
    score = sum([winnerDeck[i] * (len(winnerDeck) - i) for i in range(len(winnerDeck))])
    print(f"Final score: {score}")


if __name__ == '__main__':
    main()