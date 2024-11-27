import os
import random

from zmq import has
from art import logo, vs
from game_data import data

SCORE = 0
has_game_ended = False

def choose_random(Data_list):
    random_choice = random.choice(Data_list)
    return random_choice

print(logo)
option_A = choose_random(data)

while not has_game_ended:
    
    print("Option A:", end=" ")
    for key, val in option_A.items():
        if key == "follower_count":
            continue
        else:
            print(val,end=", ")
    print("\n", vs)

    option_B = choose_random((data))
    print("Option B:", end=" ")
    
    for key, val in option_B.items():
        if key == "follower_count":
            continue
        else:
            print(val,end=", ")

    user_input = input("\nWho has more followers? Type 'A' or 'B': ")

    if user_input == "A" or user_input == "a":
        if option_A["follower_count"] > option_B["follower_count"]:
            SCORE += 1
            os.system("cls")
            print(f"You are right. Your score is {SCORE}")
            option_A = option_B 
        else:
            os.system("cls")
            print(f"You are wrong. Your score is {SCORE}")  
            has_game_ended = True
  

    elif user_input == "B" or user_input == "b":
        if option_A["follower_count"] < option_B["follower_count"]:
            SCORE += 1
            os.system("cls")
            print(f"You are right. Your score is {SCORE}") 
            option_A = option_B   
        else:
            os.system("cls")
            print(f"You are wrong. Your score is {SCORE}")
            has_game_ended = True
    else:
        print("Wrong Option")
        print(f"Your score is {SCORE}")

        has_game_ended = True