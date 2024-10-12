print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
\n''')

print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.")

direction = input('You are at a cross road. Where do you want to go? Type "Left" or "Right"\n')

if direction == "Left" or direction == "left":
    moving_forward = input('You reached a lake. There is an island ahead in the middle of lake. Type "wait" for boat or "swim" to swim across the river\n')
    if moving_forward == "wait" or moving_forward == "Wait":
        island = input('You arrived at the island unharmed. There is a house with 3 doors. One "Red", one "Yellow" and one "Blue". Choose your color:\n')
        if island == "Blue"     or island == "blue":
            print("You entered the house and found a staircase which led you to the treasure. YOU WON!")
        elif island == "Red" or island == "red":
            print("You entered the beast room. Game Over :)")
        else:
            print("You were found by house owner. Game Over :)") 
    else:
        print("You tried to swim and were drowned by the strong current. Game Over :)")
else:
    print("You turned right where there was no further road to move. Game Over :)")