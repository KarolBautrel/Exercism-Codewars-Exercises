SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def superlist(a, b):
    return str(b) in str(a)


def sublist(a, b):
    return str(a) in str(b)


def check_list(a, b):
    sub = sublist(a, b)
    sup = superlist(a, b)

    if sub and sup:
        return EQUAL
    elif sup:
        return SUPERLIST
    elif sub:
        return SUBLIST
    else:
        return UNEQUAL


print(check_list([1, 2], [1, 22]))
