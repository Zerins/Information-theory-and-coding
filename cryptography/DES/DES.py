from encryption_func import encryption_f, XOR
import numpy as np

def keys_generation(user_key):
    C0_matrix = [57, 49, 41, 33,25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]
    D0_matrix = [63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    LCS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    permutation = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

    C0 = []
    D0 = []
    for i in range(28):
        C_bit = user_key[C0_matrix[i]-1]
        C0.append(C_bit)
        D_bit = user_key[D0_matrix[i]-1]
        D0.append(D_bit)
    C_list = [C0]
    D_list = [D0]
    round_keys = []
    for i in range(1, 17):
        left_shifted_bits_num = LCS[i-1]
        C = C_list[i-1].copy()
        D = D_list[i-1].copy()
        for k in range(left_shifted_bits_num):
            C_bit = C.pop(0)
            C.append(C_bit)
            D_bit = D.pop(0)
            D.append(D_bit)
        C_list.append(C)
        D_list.append(D)
        new_matrix = C + D
        key = []
        for j in range(48):
            bit = new_matrix[permutation[j]-1]
            key.append(bit)
        round_keys.append(key)

    return round_keys

def DES_encryption(input_block, user_key):
    matrix_IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    inverse_IP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

    L0 = []
    R0 = []
    for i in range(32):
        L_bit = input_block[matrix_IP[i]-1]
        R_bit = input_block[matrix_IP[i+32]-1]
        L0.append(L_bit)
        R0.append(R_bit)
    L_list = [L0]
    R_list = [R0]
    round_keys = keys_generation(user_key)
    for i in range(16):
        R = R_list[i]
        L = L_list[i]
        K = round_keys[i]
        func_result = encryption_f(R, K)
        xor_block = []
        for k in range(32):
            xor = XOR(L[k], func_result[k])
            xor_block.append(xor)
        L = R
        R = xor_block
        L_list.append(L)
        R_list.append(R)
    final = L_list[16] + R_list[16]
    output_block = []
    for num in inverse_IP:
        bit = final[num-1]
        output_block.append(bit)

    return output_block
