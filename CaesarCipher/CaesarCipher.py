from CaesarCipherArt import logo

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(text, shift, direction):
    cipher_text = ""
    plain_text = ""
    
    for letter in text:
        if letter in alphabets:
            position = alphabets.index(letter)
            if direction == 'encode':
                new_position = (position + shift) % 26
                cipher_text += alphabets[new_position]
            elif direction == 'decode':
                new_position = (position - shift) % 26
                plain_text += alphabets[new_position]
        else:

            if direction == 'encode':
                cipher_text += letter
            if direction == 'decode':
                plain_text += letter

    if direction == 'encode':
        print(f"The encrypted text is: {cipher_text}")
    elif direction == 'decode':
        print(f"The decrypted text is: {plain_text}")

print(logo)
exits = True

while exits:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt\n").lower().strip()
    message = input("Type your message:\n").lower()
    shift = int(input("Input the shift number:\n"))

    ceaser(text=message, shift=shift, direction=direction)

    finished = input("Type 'yes' to continue and 'no' to exit\n").lower()
    if finished == 'no':
        exits = False
        print("Goodbye!")
