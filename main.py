import random
from art import logo

def picking_cards(player_or_banker):
    new_card=""
    new_card=random.sample(cards,1)
    for card in new_card:
        player_or_banker.append(card)
    return player_or_banker
def cards_counter(player_or_banker):
    total = 0
    for card in player_or_banker:
        if card=="king" or card=="queen" or card=="jack":
            total+=10
        elif type(card)==int:
            total+=card
        elif card=="ace":
            total +=11 if total+11<= 21 else 1
    return total
def banks_picking(bank_choice):
    while cards_counter(bank_choice)<17:
        picking_cards(banker)
    print(f"Computer's final hand: {banker}, final score: {cards_counter(banker)}")
    return cards_counter(bank_choice)

def compare(a,b):
    if a>b and a<=21:
        print("Player Wins")
    elif b>a and b<=21:
        print("Computer Wins")
    elif a==b:
        print("Draw 🙃")
    elif b>21:
        print("Banker Busted-Player Wins")
def more_cards():
    hit_other_card=input("Type 'y' to get another card, type 'n' to pass:")
    if hit_other_card == "y" and cards_counter(player)<=21:
        picking_cards(player)
        print(f"your cards: {player}, your score : {cards_counter(player)}")
        more_cards()
    else:
        print(f"Your final hand: {player}, final score: {cards_counter(player)}")
        if cards_counter(player) > 21:
            print("player busted-Computer Wins!!")
        elif cards_counter(player) <= 21:
            if cards_counter(banker) > 17:
                print(f"Computer's final hand: {banker}, final score: {cards_counter(banker)}")
                compare(cards_counter(player), cards_counter(banker))
            else:
                banks_picking(banker)
                compare(cards_counter(player), cards_counter(banker))


def blackjack_game():
    print(logo)
    print(f"your cards: {player}, your score : {cards_counter(player)}")
    print(f"computer's first card: {banker[0]}")
    more_cards()
    new_game()

def new_game():
    new_game=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if new_game=="y":
        print("\n"*25)
        blackjack_game()
    else:
        print("Thanks for coming !!")

cards=[2,3,4,5,6,7,8,9,10,"king","queen","jack","ace"]
banker=random.sample(cards,2)
player=random.sample(cards,2)
new_game()



