from alphabet import alphabet


def caesar(text, shift, direction):
    end_text = ''
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction} text is {end_text}")