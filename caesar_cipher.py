"""
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift,
is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number
of positions down the alphabet.
For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
The method is named after Julius Caesar, who used it in his private correspondence.[1]

Source: https://en.wikipedia.org/wiki/Caesar_cipher
"""

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