from logo_art import logo
from replay_func import replay
from caesar_func import caesar
print(logo)

while True:
    decode_on = input("Ready to decode/encode? Input Yes or No: \n ").lower()
    if decode_on == "yes":
        decode_on = True
    else:
        print("Come back when ready!")
        break
    direction_answer = ["encode","decode"]
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction not in direction_answer:
        direction = input("Sorry,type 'encode' to encrypt, type 'decode' to decrypt:\n")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(text, shift, direction)
    if not replay():
        print("Thank you!")
        break
