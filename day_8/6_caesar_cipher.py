from string import ascii_lowercase


def encrypt(plaintext: str, shift: int):
    encrypted_message = ""
    for char in plaintext:
        index = ascii_lowercase.index(char) + shift  # shifted index
        if (
            index > len(ascii_lowercase) - 1
        ):  # if char reach to the end , go back to start from beginning (a, b, ..)
            index = index - len(ascii_lowercase)
        encrypted_message += ascii_lowercase[index]
    return encrypted_message


def decrypt(encrypted_text: str, shift: int):
    original_message = ""
    for char in encrypted_text:
        original_index = ascii_lowercase.index(char) - shift
        if (
            original_index < 0
        ):  # if char reach to the beginning , go back to start from the end (z, y, ..)
            original_index = original_index + len(ascii_lowercase)
        original_message += ascii_lowercase[original_index]
    return original_message


def main():
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt")
    text = input("Type Yor message").lower()
    shift = int(input("Type the shift number"))
    if direction == "encode":
        print(encrypt(text, shift=shift))
    elif direction == "decode":
        print(decrypt(text, shift))
    else:
        print(f"Invalid option please type 'encode' or 'decode'")


if __name__ == "__main__":
    main()
