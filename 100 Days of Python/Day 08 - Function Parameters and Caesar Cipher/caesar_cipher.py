# Caesar Cipher
# By Marco Redulla
# Day 8 (19/06/2024)
import caesar_art

# For the bounds, refer to Python Decimal Unicode index
def char_shift(char, bounds, cmd, shift):
    if cmd == 'encode':
        new_char = ord(char) + shift
        if new_char > bounds:
            new_char -= 26
    elif cmd == 'decode':
        new_char = ord(char) - shift
        if new_char < bounds:
            new_char += 26
    return chr(new_char)


def cipher(message, shift, cmd):
    new_message = list(message)
    if cmd == 'encode':
        for i in range(len(new_message)):
            if new_message[i].isalpha():
                if new_message[i].isupper():
                    new_message[i] = char_shift(char=message[i], bounds=90, cmd='encode',shift=shift)
                else:
                    new_message[i] = char_shift(char=message[i], bounds=122, cmd='encode',shift=shift)
        print(f"Here's the encoded result: {''.join(new_message)}")
    else:
        for i in range(len(message)):
            if new_message[i].isalpha():
                if new_message[i].isupper():
                    new_message[i] = char_shift(char=message[i], bounds=65, cmd='decode',shift=shift)
                else:
                    new_message[i] = char_shift(char=message[i], bounds=97, cmd='decode',shift=shift)
        print(f"Here's the decoded result: {''.join(new_message)}")
    return new_message

def caesar_cipher():
    cmd = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if cmd != 'encode' and cmd != 'decode':
        reset = input("Invalid command. Try again? (Y/N) ").lower()
        if reset == 'y':
            caesar_cipher()
    else:
        message = input("Type your message below:\n")
        shift = int(input("Type the shift number below:\n"))
        if shift > 25:
            reset = input("The maximum shift is 25. Try again? (Y/N) ").lower()
            if reset == 'y':
                caesar_cipher()
        cipher(message=message, shift=shift, cmd=cmd)
        reset = input("Would you like to try again? (Y/N) ").lower()
        if reset == 'y':
            caesar_cipher()

# Main Code
print(caesar_art.logo)
caesar_cipher()
