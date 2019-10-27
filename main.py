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

    def handle_ace(player, card):
        if player.get_points() < winning_points - 11:
            return card[1]
        else:
            return card[0]

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
            return True
        elif dealer.get_points() > player.get_points() and not dealer.get_points() > winning_points:
            print("Dealer wins")
            return True
        elif dealer.get_points() > winning_points:
            player.balance += pot_size
            print("player wins")
            return True
        elif player.get_points() > winning_points:
            print("dealer wins")
            return True
        elif player.get_points() == dealer.get_points() and(player.get_points() and dealer.get_points()) < winning_points:
            print("dealer wins")
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

    choice = game_player.hit_stay_bet(deal_cards)
    if choice == "stayed":
        player_stayed = True
    else:
        pot_size = choice

    if player_stayed:
        if game_dealer.get_points() < winning_points and game_dealer.get_points() < game_player.get_points():
            deal_cards(game_dealer)
        else:
            end_round(game_player, game_dealer)

    turn += 1
    if player_stayed:
        if end_round(game_player, game_dealer):
            end_game = input("continue playing? (y, n)").lower()
            if end_game == "n":
                game_round += 1
            else:
                play = False
