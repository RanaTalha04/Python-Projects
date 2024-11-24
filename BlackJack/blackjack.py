import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(List):
    """Returns random number from the list"""
    card = random.choice(List)
    return card

def calculate_score(List):
    """Returns the sum of list"""
    result = sum(List)

    if 11 in List and 10 in List and len(cards) == 2:
        return 0
    if 11 in List and result > 21:
        List.remove(11)
        List.append(1)
    return result

def compare(user, computer):
    """Compare two value and returns a string"""
    if user == computer:
        return ("Draw")
    elif user > 21:
        return ("You Loose. Score exceeds.")
    elif computer > 21:
        return ("You Win. Computer's score exceeds.")
    elif user == 0:
        return ("You Win. BLACKJACK")
    elif computer == 0:
        return ("You Loose. Computer has a BLACKJACK")
    elif user > computer:
        return ("You Win")
    else:
        return ("You Loose.")

def Play_Game():
    
    print(logo)
 
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards(cards))
        computer_cards.append(deal_cards(cards))

    while not is_game_over:
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {[computer_cards[0]]}")

        if user_score == 0 or computer_score == 0 or user_score >= 21:
            is_game_over = True
        else:
            choice = input("Type 'y' for another card, type 'n' to pass ")

            if choice == 'y':
                user_cards.append(deal_cards(cards))
            else:
                is_game_over = True
    
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_cards(cards))
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {user_cards}, current score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, current score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Type 'y' to play the game, type 'n' to exit. ") == 'y':
    os.system("cls")
    Play_Game()