import random
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

is_Found = False
random_number = random.randint(1, 100)

print(logo)

print("Welcome to Number Guessing Game ")
print("I am thinking of a number between 1 and 100 ")

choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

while not is_Found:

    if choice == "easy":
        print(f"You have {EASY_ATTEMPTS} attempts remaining to guess the number.")
        guess = int(input("Guess a number: "))

        if EASY_ATTEMPTS == 0:
            is_Found = True
        if guess > random_number:
            print("Too high")
            EASY_ATTEMPTS -= 1
        elif guess < random_number:
            print("Too low")
            EASY_ATTEMPTS -= 1
        else:
            is_Found = True
            print("You guessed it right. You won")

    elif choice == "hard":
        print(f"You have {HARD_ATTEMPTS} attempts remaining to guess the number.")
        guess = int(input("Guess a number: "))

        if HARD_ATTEMPTS == 0:
            is_Found = True
        if guess > random_number:
            print("Too high")
            HARD_ATTEMPTS -= 1
        elif guess < random_number:
            print("Too low")
            HARD_ATTEMPTS -= 1
        else:
            is_Found = True
            print("You guessed it right. You won")
    else:
        print("Invalid Choice")
        is_Found = True