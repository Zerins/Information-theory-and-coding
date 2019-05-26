def caesar_cipher(plaintext, k):
    # k ranges from 1 to 25
    # a-0, b-1, z-25
    plaintext = plaintext.lower()
    ciphertext = ''
    for letter in plaintext:
        if (ord(letter) < 97) or (ord(letter) > 122):
            new_letter = letter
        else:
            M = ord(letter) - 97
            C = (M + k) % 26
            asc_C = C + 97
            new_letter = chr(asc_C)
        ciphertext = ciphertext + new_letter

    return ciphertext


if __name__ == "__main__":
    k = 3
    with open('plaintext.txt') as object:
        plaintext = object.read()
    with open('ciphertext.txt', 'w') as object:
        ciphertext = caesar_cipher(plaintext, k)
        object.write(ciphertext)
