def multi(x: list, y: list):
    if x == [0] or y == [0]:
        return [0]

    # switch x and y if y > x
    if len(y) > len(x):
        x, y = y, x

    # create table for multiplications before adding
    z = [None] * len(y)
    for i in range(len(y)):
        z[i] = [0] * (len(x) + len(x))

    # transfer for multiplications
    transfer = [0] * (len(x) + 1)

    # fill z table with multiplications
    for y0 in range(len(y)):
        for x0 in range(len(x)):
            multiplication = y[y0] * x[x0]
            if transfer[x0]:
                multiplication += transfer[x0]
            transfer[x0] = 0
            z[y0][x0+y0] = multiplication % 10
            transfer[x0+1] = multiplication // 10
        if transfer[len(x)]:
            z[y0][len(x)+y0] = transfer[len(x)]
            transfer[len(x)] = 0

    # create table for multiplications' sum
    output = [0] * (len(max(z)) + 1)
    # transfer for sum
    transfer_out = [0] * (len(max(z)) + 1)

    # count output
    for position in range(len(max(z))):
        temp_sum = 0
        for line in range(len(y)):
            temp_sum += z[line][position]
        temp_sum += transfer_out[position]
        output[position] = temp_sum % 10
        transfer_out[position+1] = temp_sum // 10

    # check for last transfer
    if transfer_out[len(max(z))]:
        output[len(max(z))] = transfer_out[len(max(z))]

    # remove zeros
    while output[len(output)-1] == 0:
        output.pop()

    return output


def list_to_string(l: list):
    s = ""
    for i in reversed(l):
        s += str(i)
    return s


def int_to_list(i: int):
    if i == 0:
        return [0]
    output = []
    while i != 0:
        output.append(i % 10)
        i = i // 10
    return output


def string_factorial(x: int):
    output = [1]
    for i in range(x):
        output = multi(output, int_to_list(i+1))
    return list_to_string(output)


if __name__ == '__main__':
    print(string_factorial(500))
