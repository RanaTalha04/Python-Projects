import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '#', '$', '%', '&', '*', '(', ')','+','_']

password = []

print("Welcome to PyPassword Generator! ")

input_letters = int(input("How many letters would you like in your password? "))
input_numbers = int(input("How many numbers would you like in your password? "))
input_special = int(input("How many special characters would you like in your password? "))

input_password = input_letters + input_numbers + input_special
for letter in range(0,input_letters):
    password.append(random.choice(letters))
    
for number in range(0,input_numbers):
    password.append(random.choice(numbers))

for character in range(0,input_special):
    password.append(random.choice(special_characters))

random.shuffle(password)

password_str = ""

for char in password:
    password_str += char

print(f"Your password is: {password_str}")

