"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import re
import string


def camel_cards():
    # Getting data and parsing
    with open("input.txt") as f:
        data = f.read().strip().split("\n")

    hands = [Hand(hand.split(" ")[0], hand.split(" ")[1]) for hand in data]    

    # Ranking the hands
    hands.sort(key=lambda x: (x.type, x.hand_strength()))

    # Calculating the total winnings
    total_winning = 0
    for i, hand in enumerate(hands):
        total_winning += (i+1) * hand.bid

    return total_winning


class Hand:
    CARDS_STRENGTH = "23456789TJQKA"

    HIGH_CARD  = 0
    ONE_PAIR   = 1
    TWO_PAIR   = 2
    THREE_KIND = 3
    FULL_HOUSE = 4
    FOUR_KIND  = 5
    FIVE_KIND  = 6

    def __init__(self, hand: str, bid: str) -> None:
        self.hand = hand
        self.bid = int(bid)
        self.type = self.get_type()

    # Returns the type this hand
    def get_type(self):
        labels_count = dict()

        for label in self.hand:
            labels_count[label] = self.hand.count(label)
        
        max_occ = max(labels_count.values())
        if max_occ == 5: return self.FIVE_KIND
        if max_occ == 4: return self.FOUR_KIND

        if max_occ == 3:
            if min(labels_count.values()) == 2: 
                return self.FULL_HOUSE
            else:
                return self.THREE_KIND
        
        if max_occ == 2:
            if len(labels_count.keys()) == 3:
                return self.TWO_PAIR
            else:
                return self.ONE_PAIR

        return self.HIGH_CARD


    # Returns an encoded version of self.hand based on CARDS_STRENGTH
    # Used for comparison
    def hand_strength(self):
        enc = ""

        for char in self.hand:
            enc += str(string.ascii_lowercase[self.CARDS_STRENGTH.index(char)])

        return enc

if __name__ == '__main__':
    print(camel_cards())
