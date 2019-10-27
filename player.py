from functools import reduce


class Player():
    def __init__(self, balance):
        self.balance = balance
        self.cards = []

    def player_move(self):
        return input("would you like to hit or stay").lower()

    def get_points(self):
        return reduce(lambda card, next_card: card + next_card, self.cards, 0)

    def hit_stay_bet(self, deal):
        print("1: hit")
        print("2: stay")
        print("3: bet")
        choice = input(": ")
        if choice == "1":
            deal(self)
        elif choice == "2":
            return "stayed"
        elif choice == "3":
            bet_amt = int(input("enter amount: "))
            while bet_amt > self.balance:
                bet_amt = input("enter amount")
            self.balance = self.balance - bet_amt
            return bet_amt * 2
        else:
            self.hit_stay_bet()
