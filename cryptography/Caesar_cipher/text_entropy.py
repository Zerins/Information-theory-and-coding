import math
from Caesar_cipher import caesar_cipher

def text_entropy(text):
    text = text.lower()
    total_len = 0
    letter_list = [0] * 26
    for letter in text:
        if (ord(letter) >= 97) and (ord(letter) <= 122):
            pos = ord(letter) - 97
            letter_list[pos] += 1
            total_len += 1
    entropy = 0
    for num in letter_list:
        prob = num / total_len
        if prob == 0:
            s = 0
        else:
            surprise = (-1) * math.log(prob, 2)
            s = prob * surprise
        entropy += s

    return entropy


if __name__ == "__main__":
    k = 3
    with open("example_file.txt") as object:
        plaintext = object.read()
        M_entropy = text_entropy(plaintext)
        ciphertext = caesar_cipher(plaintext, k)
        C_entropy = text_entropy(ciphertext)
    print(M_entropy)
    print(C_entropy)
