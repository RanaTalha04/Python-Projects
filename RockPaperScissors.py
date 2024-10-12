import random

rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
your_turn = int(input('What do you choose? Type "0" for "Rock", "1" for "Paper" and "2" for "Scissors" '))
computer_turn = random.randint(0,2)

if your_turn == computer_turn == 0:
    print("Your choice: ")
    print(rock)

    print("Computer's choise: ")
    print(rock)

    print("Game Draw.")

elif your_turn == 1 and computer_turn == 1:
    print("Your choice: ")
    print(paper)

    print("Computer's choise: ")
    print(paper)

    print("Game Draw.")

elif your_turn == 2 and computer_turn == 2:
    print("Your choice: ")
    print(scissors)

    print("Computer's choise: ")
    print(scissors)

    print("Game Draw.")

elif your_turn == 0 and computer_turn == 1:
    print("Your choice: ")
    print(rock)

    print("Computer's choise: ")
    print(paper)

    print("You Lose.")

elif your_turn == 0 and computer_turn == 2:
    print("Your choice: ")
    print(rock)

    print("Computer's choise: ")
    print(scissors)

    print("You Won.")

elif your_turn == 1 and computer_turn == 0:
    print("Your choice: ")
    print(paper)

    print("Computer's choise: ")
    print(rock)

    print("You Won.")

elif your_turn == 1 and computer_turn == 2:
    print("Your choice: ")
    print(paper)

    print("Computer's choise: ")
    print(scissors)

    print("You Loss.")

elif your_turn == 2 and computer_turn == 0:
    print("Your choice: ")
    print(scissors)

    print("Computer's choise: ")
    print(rock)

    print("You Loss.")

elif your_turn == 2 and computer_turn == 1:
    print("Your choice: ")
    print(scissors)

    print("Computer's choise: ")
    print(paper)

    print("You Won.")

else: 
    print("\nYou choose wrong option....")