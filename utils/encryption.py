import string
import numpy as np
np.random.seed(30)


def caesar_cipher(plainText):
    """
    Args:
    plainText(string): Text to be encrypted
    key(int): Shift value for Caesar Cipher
    """
    key = np.random.randint(low=1, high=26)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    shifted_alphabet = alphabet[26-key:]+alphabet[0:(26-key)]
    shifted_number = numbers[10-key:]+numbers[0:(10-key)]
    cipher_text = ""

    for i in range(len(plainText)):
        char = plainText[i]
        if(char.isalpha()):
            idx = alphabet.find(char.upper())
            if idx == -1:
                cipher_text = cipher_text + char
            elif char.islower():
                cipher_text = cipher_text + shifted_alphabet[idx].lower()
            else:
                cipher_text = cipher_text + shifted_alphabet[idx]

        elif(char.isnumeric()):
            idx = numbers.find(char.upper())
            if idx == -1:
                cipher_text = cipher_text + char
            else:
                cipher_text = cipher_text + shifted_number[idx]

    return (cipher_text, key)


if __name__ == "__main__":
    file = open('data/rockyou.txt', 'r')
    count = 0
    for x in file:
        count += 1
        print(x)
        print(caesar_cipher(x, 1))
        if count == 6:
            break
