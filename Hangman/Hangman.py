from genericpath import exists
import random
from HangmanWord_list import word_list
from HangmanArt import stages,logo

print(logo)
display = []

chosen_word = random.choice(word_list)
print(chosen_word)

for char in range(0,len(chosen_word)):
    display += "_"

end_of_game = False
lives = 6

while not end_of_game or lives > 0:
  guess = input("Enter character: ").lower()

  if guess in display:
    print(f"{guess} already exists in the word.")

  for index in range(0, len(chosen_word)):
    if chosen_word[index] == guess:
      display[index] = guess

  if guess not in chosen_word:
    print(f"Character {guess} is not in the word, You lost a life :)")
    print(stages[lives - 1])
    lives -= 1

    if lives == 0:
      print(f"The word is: {chosen_word}")
      print("You Loose") 
      break

  print(f"{' '.join(display)}")
  
  if "_" not in display:
   end_of_game = True 
   print("You Won")