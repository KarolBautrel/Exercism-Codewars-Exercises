def convert_to_binary(a, b):
    sum = a+b
    binaryList = []
    while sum >= 1:
        if sum % 2 == 1:
            binaryList.append(str(1))
        else:
            binaryList.append(str(0))
        sum = int(sum)//2

    print(binaryList)
    binaryList = list(reversed(binaryList))
    print(binaryList)
    return ''.join(binaryList)


print(convert_to_binary(453717338523405869254990822, 359853738140598360318802514))


def add_binary(a, b):
    return convert_to_binary(a, b)


def DecimalToBinary(a, b):
    return bin(a+b)[2:]


print(bin(4 + 15))
