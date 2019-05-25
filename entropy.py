import math

def marginal(data, method, x_num, y_num):
    """
        if method == 0, P(y)
        if method == 1, P(x)
    """
    marginal_prob = []
    if method == 0:
        for list in data:
            prob_y = sum(list)
            marginal_prob.append(prob_y)
    elif method == 1:
        for i in range(x_num):
            prob_x = 0
            for j in range(y_num):
                prob_x += data[j][i]
            marginal_prob.append(prob_x)

    return marginal_prob

def joint_entropy(data):
    entropy = 0
    for list in data:
        for prob in list:
            if prob == 0:
                s = 0
            else:
                surprise = (-1) * math.log(prob, 2)
                s = surprise * prob
            entropy += s

    return entropy

def conditional_entropy(data, method):
    """
        if method == 0, H(X|Y)
        if method == 1, H(Y|X)
    """
    y_num = len(data)
    x_num = len(data[0])

    entropy = 0
    for i in range(y_num):
        for j in range(x_num):
            marginal_prob = marginal(data, method, x_num, y_num)
            if data[i][j] == 0:
                s = 0
            else:
                if method == 0:
                    margin = data[i][j] / marginal_prob[i]
                elif method == 1:
                    margin = data[i][j] / marginal_prob[j]
                surprise = (-1) * math.log(margin, 2)
                s = data[i][j] * surprise
            entropy += s

    return entropy

def mutual_information(data):
    y_num = len(data)
    x_num = len(data[0])
    marginal_x = marginal(data, 1, x_num, y_num)
    marginal_y = marginal(data, 0, x_num, y_num)
    mutual_info = 0
    for i in range(y_num):
        for j in range(x_num):
            if data[i][j] == 0:
                func = 0
            else:
                mutual = data[i][j] / (marginal_x[j] * marginal_y[i])
                func = data[i][j] * math.log(mutual, 2)
            mutual_info += func

    return mutual_info

def variable_entropy(data, method):
    """
        if method == 0, H(y)
        if method == 1, H(x)
    """
    y_num = len(data)
    x_num = len(data[0])
    if method == 0:
        marginal_y = marginal(data, 0, x_num, y_num)
        entropy = 0
        for i in range(y_num):
            if marginal_y[i] == 0:
                s = 0
            else:
                surprise = (-1) * math.log(marginal_y[i], 2)
                s = marginal_y[i] * surprise
            entropy += s
    elif method == 1:
        marginal_x = marginal(data, 1, x_num, y_num)
        entropy = 0
        for i in range(x_num):
            if marginal_x[i] == 0:
                s = 0
            else:
                surprise = (-1) * math.log(marginal_x[i], 2)
                s = marginal_x[i] * surprise
            entropy += s

    return entropy

if __name__ == "__main__":
    XY_list = [
        [1/8, 1/16, 1/32, 1/32],
        [1/16, 1/8, 1/32, 1/32],
        [1/16, 1/16, 1/16, 1/16],
        [1/4, 0, 0, 0]]

    joint = joint_entropy(XY_list)
    condxy = conditional_entropy(XY_list, 0)
    condyx = conditional_entropy(XY_list, 1)
    mutual_info = mutual_information(XY_list)
    entropy_x = variable_entropy(XY_list, 1)
    entropy_y = variable_entropy(XY_list, 0)
    print("H(X, Y) =  ", joint)
    print("H(X|Y) = ", condxy)
    print("H(Y|X) = ", condyx)
    print("I(X;Y) = ", mutual_info)
    print("H(X) = ", entropy_x)
    print("H(Y) = ", entropy_y)
