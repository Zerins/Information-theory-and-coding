def letter_analysis(ciphertext):
    ciphertext = ciphertext.lower()
    total_len = 0
    letter_list = [0] * 26
    for letter in ciphertext:
        if (ord(letter) >= 97) and (ord(letter) <= 122):
            pos = ord(letter) - 97
            letter_list[pos] += 1
            total_len += 1
    prob_list = []
    for num in letter_list:
        prob = num / total_len
        prob_list.append(prob)
    letter_dict = {chr(i+97): prob_list[i] for i in range(26)}
    letter_dict = sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)

    return letter_dict

def n_gram_analysis(ciphertext, n):
    k = n - 1
    ciphertext = ciphertext.lower()
    cipher_str = ''
    for letter in ciphertext:
        if (ord(letter) >= 97) and (ord(letter) <= 122):
            cipher_str += letter
    total_num = len(cipher_str) - k
    n_gram_list = []
    count_list = []
    for i in range(len(cipher_str)-k):
        n_gram = ''
        for j in range(i, i+n):
            n_gram += cipher_str[j]
        if n_gram in n_gram_list:
            idx = n_gram_list.index(n_gram)
            count_list[idx] += 1
        else:
            n_gram_list.append(n_gram)
            count_list.append(1)
    prob_list = []
    for num in count_list:
        prob = num / total_num
        prob_list.append(prob)
    n_gram_dict = {n_gram_list[i]: prob_list[i] for i in range(len(n_gram_list))}
    n_gram_dict = sorted(n_gram_dict.items(), key=lambda x: x[1], reverse=True)

    return n_gram_dict


if __name__ == "__main__":
    with open('ciphertext.txt') as object:
        ciphertext = object.read()
        letter_dict = letter_analysis(ciphertext)
        bigram_dict = n_gram_analysis(ciphertext,2)
        trigram_dict = n_gram_analysis(ciphertext, 3)
        print(letter_dict)
        print('\n')
        print(bigram_dict)
        print('\n')
        print(trigram_dict)
