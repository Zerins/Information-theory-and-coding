def XOR(bit1, bit2):
    xor = (bit1 + bit2) % 2
    return xor

def XOR_list(bit_list):
    bit1 = bit_list[0]
    bit2 = bit_list[1]
    for i in range(2, len(bit_list)):
        bit1 = XOR(bit1, bit2)
        bit2 = bit_list[i]
    xor = XOR(bit1, bit2)

    return xor

def redundant_bits(data_bits_num):
    redundant_num = 0
    while (2 ** redundant_num < data_bits_num + redundant_num + 1):
        redundant_num += 1

    return redundant_num

def redundant_pos_list(redundant_num):
    pos_list = []
    for i in range(redundant_num):
        pos = 2 ** i - 1
        pos_list.append(pos)

    return pos_list

def even_parity(redundant_pos, total_bits, code_list):
    interval = redundant_pos + 1
    initial_pos = redundant_pos
    sum_of_one = 0
    for i in range(initial_pos, total_bits, (interval*2)):
        for k in range(interval):
            pos = i + k
            if pos > (total_bits-1):
                break
            bit = code_list[pos]
            sum_of_one += bit
    if sum_of_one % 2 == 1:
        code_list[redundant_pos] = 1

    return code_list

def hamming(data_bits_list):
    data_bits_num = len(data_bits_list)
    redundant_num = redundant_bits(data_bits_num)
    pos_list = redundant_pos_list(redundant_num)
    for pos in pos_list:
        data_bits_list.insert(pos, 0)
    total_bits = len(data_bits_list)
    code_list = data_bits_list
    for pos in pos_list:
        code_list = even_parity(pos, total_bits, code_list)

    return code_list

def single_error_detection(code_list):
    redundant_num = 0
    total_bits = len(code_list)
    num = total_bits
    while num != 0:
        num //= 2
        redundant_num += 1
    pos_list = redundant_pos_list(redundant_num)
    binary_list = []
    for redundant_pos in pos_list:
        interval = redundant_pos + 1
        initial_pos = redundant_pos
        bit_list = []
        for i in range(initial_pos, total_bits, (interval*2)):
            for k in range(interval):
                pos = i + k
                if pos > (total_bits-1):
                    break
                bit = code_list[pos]
                bit_list.append(bit)
        xor = XOR_list(bit_list)
        binary_list.append(xor)
    error_pos = binary_list[0] * (2 ** 0)
    for j in range(1, len(binary_list)):
        binary = binary_list[j]
        error_pos = error_pos + (binary * (2 ** j))
    error_pos -= 1
    return error_pos

def single_error_correction(code_list):
    error_pos = single_error_detection(code_list)
    if error_pos != (-1):
        code_list[error_pos] = 1 - code_list[error_pos]

    return code_list

def double_error_detection(code_list):
    error_pos = single_error_detection(code_list)
    parity_bit = XOR_list(code_list)
    code_list.insert(0, parity_bit)
    if error_pos == (-1):
        if parity_bit == 0:
            return "No error"
        elif parity_bit == 1:
            code_list.pop(0)
            return code_list
    else:
        if parity_bit == 0:
            return "Double error"
        else:
            code_list.pop(0)
            code_list[error_pos] = 1 - code_list[error_pos]
            return code_list

if __name__ == "__main__":
    code_list = hamming([1, 0, 0, 1, 1, 0, 1])
    print(code_list)
    error_list = [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1]
    error_pos = single_error_detection(error_list)
    print(error_pos)
    code_list = single_error_correction(error_list)
    print(code_list)
