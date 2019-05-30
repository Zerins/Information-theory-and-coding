import math

def codeword_func(fraction, k):
    # convert decimal fraction to binary
    binary_str = ''
    for i in range(k):
        convert = fraction * 2
        binary_digit = math.floor(convert)
        binary_str += str(binary_digit)
        fraction = convert - binary_digit

    return binary_str

def shannon_fano_elias(prob_list):
    length = len(prob_list)
    l_list = []
    for prob in prob_list:
        l = math.ceil(math.log(1/prob, 2) + 1)
        l_list.append(l)
    F_list = [prob_list[0]]
    decimal_list = [0.5 * prob_list[0]]
    first_codeword = codeword_func(decimal_list[0], l_list[0])
    codeword_list = [first_codeword]
    for i in range(1, length):
        F = F_list[i-1] + prob_list[i]
        decimal = F_list[i-1] + 0.5 * prob_list[i]
        codeword = codeword_func(decimal, l_list[i])
        F_list.append(F)
        decimal_list.append(decimal)
        codeword_list.append(codeword)

    return F_list, decimal_list, codeword_list


if __name__ == "__main__":
    x_list = [1, 2, 3, 4, 5]
    prob_list = [0.25, 0.25, 0.2, 0.15, 0.15]
    F_list, decimal_list, codeword_list = shannon_fano_elias(prob_list)
    print(F_list)
    print(decimal_list)
    print(codeword_list)
