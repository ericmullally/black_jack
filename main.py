from dealer import Dealer
from player import Player


player_balance = float(input("please provide a balance (100 - 1000) "))
play = True
game_round = 0


while player_balance < 100 or player_balance > 1000:
    print("please choose an amount between 100 - 1000")
    player_balance = float(input("please provide a balance (100 - 1000) "))

turn = 0
game_dealer = Dealer()
game_player = Player(player_balance)
winning_points = 21
pot_size = 0
player_stayed = False

while play == True:
    def dealer_continue():
        return (game_dealer.get_points(
        ) < winning_points and game_dealer.get_points() < game_player.get_points())

    def handle_ace(player, card):
        if player.get_points() < winning_points - 11:
            return card[1]
        else:
            return card[0]

    # handle negative card count in dealer
    def deal_cards(player):
        card = game_dealer.deal()
        if type(card) == list:
            player.cards.append(handle_ace(player, card))
        else:
            player.cards.append(card)

    def end_round(player, dealer):
        global play
        if player.get_points() > dealer.get_points() and not player.get_points() > winning_points:
            player.balance += pot_size
            print("player wins")
            print(f"your balance is {player.balance}")
            return True
        elif dealer.get_points() > player.get_points() and not dealer.get_points() > winning_points:
            print("Dealer wins")
            print(f"your balance is {player.balance}")
            return True
        elif dealer.get_points() > winning_points:
            player.balance += pot_size
            print("player wins")
            print(f"your balance is {player.balance}")
            return True
        elif player.get_points() > winning_points:
            print("dealer wins")
            print(f"your balance is {player.balance}")
            return True
        elif player.get_points() == dealer.get_points() and(player.get_points() and dealer.get_points()) < winning_points:
            print("dealer wins")
            print(f"your balance is {player.balance}")
            return True
        else:
            return False

    if turn == 0:
        deal_cards(game_dealer)
        deal_cards(game_player)
        deal_cards(game_dealer)
        deal_cards(game_player)

    print(
        f"dealer shows {game_dealer.cards[1:]} , your cards are{game_player.cards}")
    # check if player bust
    # if player bets ask if hit or stay again
    if not player_stayed:
        choice = game_player.hit_stay_bet()
        if choice == "stayed":
            player_stayed = True
        elif choice == "hit":
            deal_cards(game_player)
        else:
            pot_size = choice

    if dealer_continue():
        if player_stayed:
            while dealer_continue():
                deal_cards(game_dealer)
        else:
            deal_cards(game_dealer)

    turn += 1
    if player_stayed and not dealer_continue():
        if end_round(game_player, game_dealer):
            #this is confusing
            end_game = input("continue playing? (y, n)").lower()
            if end_game == "y":
                game_player.cards.clear()
                game_dealer.cards.clear()
                pot_size = 0
                turn = 0
                player_stayed = False
                game_round += 1
            else:
                play = False
