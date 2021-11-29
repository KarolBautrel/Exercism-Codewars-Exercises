SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0


def is_superlist(a, b):
    return str(b)[1:-1] in str(a)[1:-1]


def is_sublist(a, b):
    return str(a)[1:-1] in str(b)[1:-1]


def check_lists(a, b):
    sub = is_sublist(a, b)
    sup = is_superlist(a, b)
    if sub and sup:
        return EQUAL
    elif sup:
        return SUPERLIST
    elif sub:
        return SUBLIST
    else:
        return UNEQUAL
