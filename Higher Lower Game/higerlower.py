import os
import random
from art import logo, vs
from game_data import data

SCORE = 0

def choose_random(Data_list):
    random_choice = random.choice(Data_list)
    return random_choice

print(logo)

option_A = choose_random(data)
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
    else:
       os.system("cls")
       print(f"Wrong choice. Your score is {SCORE}")    

elif user_input == "B" or user_input == "b":
    if option_A["follower_count"] < option_B["follower_count"]:
       SCORE += 1
    else:
       os.system("cls")
       print(f"Wrong choice. Your score is {SCORE}")

