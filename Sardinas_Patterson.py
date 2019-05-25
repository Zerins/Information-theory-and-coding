# Sardinas-Patterson algorithm
def is_prefix(str_1, str_2):
    """
        if str_1 or str_2 is not prefix of each other, return 0
        if str_1 is prefix of str_2, return 1
        if str_2 is prefix of str_1, return 2
    """
    if len(str_1) <= len(str_2):
        if str_1 not in str_2:
            return 0
        else:
            if str_2.index(str_1) == 0:
                return 1
            else:
                return 0
    else:
        if str_2 not in str_1:
            return 0
        else:
            if str_1.index(str_2) == 0:
                return 2
            else:
                return 0

def sp(C):
    S_set = [C]
    i = 0
    while True:
        set_1 = set()
        set_2 = set()
        for code_1 in C:
            for code_2 in S_set[i]:
                if is_prefix(code_1, code_2) == 1:
                    suffix = code_2[len(code_1):]
                    set_1.add(suffix)
                elif is_prefix(code_1, code_2) == 2:
                    suffix = code_1[len(code_2):]
                    set_2.add(suffix)
        S = set_1.union(set_2)
        if i == 0:
            for code in S.copy():
                if code == '':
                    S.remove(code)
        for code in S:
            if (code in C) or (code == ''):
                return "Not uniquely decodable"
        for pre_set in S_set:
            if S == pre_set:
                return "Uniquely decodable"
        S_set.append(S)
        i += 1


if __name__ == "__main__":
    C1 = ['1', '001', '01110', '1110', '10011']
    C2 = ['01', '10', '00', '11']
    result1 = sp(C1)
    result2 = sp(C2)
    print(C1, result1)
    print(C2, result2)
