from string import ascii_lowercase


alphabet = ascii_lowercase + ascii_lowercase
print(alphabet)


def caesar(text, shift, direction="encode"):
    # if user enter 30 it means ( 1 loop '25' + 5 steps) = 5 steps
    shift = shift % 25
    end_text = ""
    if direction == "decode":
        shift = shift * -1
    elif direction != "encode":
        return
    for char in text:
        if char not in alphabet:
            end_text += char
        else:
            position = ascii_lowercase.index(char)
            new_position = position + shift
            end_text += alphabet[new_position]
    return end_text


if __name__ == "__main__":
    again = "yes"
    while again == "yes":
        direction = input("Type 'encode' to encrypt or 'decode' to decrypt")
        text = input("Type Yor message").lower()
        shift = int(input("Type the shift number"))
        result = caesar(text, shift, direction)
        if result:
            print(f"The {direction}d message is '{result}'")
        else:
            print("Invalid direction. Type 'encode' or 'decode'.")
        again = input("Do you want to repeat? Type 'yes' or 'no' ")
        if again == "no":
            print("GoodBye")
