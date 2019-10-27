import random
from functools import reduce

num_cards = {}
for card in range(0, 9):
    num_cards[f"{card + 1}"] = {"points": card + 1, "count": 4}


class Dealer():
    def __init__(self):
        self.deck = {"A": {"points": [1, 11], "count": 4}, "Q": {"points": 10, "count": 4}, "K": {
            "points": 10, "count": 4}, "J": {"points": 10, "count": 4}, "num_card": num_cards}
        self.cards = []

    def deal(self):
        cards = ["A", "K", "Q", "J", "num_card"]
        card = cards[random.randint(0, 4)]
        try:
            ctd = self.deck[card]
            if ctd["count"] <= 0:
                cards.remove(card)
                self.deal()
            ctd["count"] -= 1
            return ctd["points"]
        except KeyError:
            rand_card_num = str(random.randint(1, 9))
            ctd = self.deck[card][rand_card_num]
            if ctd["count"] <= 0:
                self.deck[card].pop(rand_card_num)
                self.deal()
            ctd["count"] -= 1
            return ctd["points"]

    def get_points(self):
        return reduce(lambda card, next_card: card + next_card, self.cards, 0)
