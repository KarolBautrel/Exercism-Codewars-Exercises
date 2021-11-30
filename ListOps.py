import itertools


def append(list1, list2):
    for i in list2:
        list1.append(i)
    return list1


print(append([], [1, 2, 3, 4]))


def concat(lists):

    return list(itertools.chain.from_iterable(lists))


print(concat([[1, 2], [3], [], [4, 5, 6]]))


def filter(function, list):
    myList = []
    for i in list:
        if function(i):
            myList.append(i)
    return myList


print(filter((lambda x: x % 2 == 1), [1, 2, 3, 5]))


def length(list):
    return len(list)


def map(function, list):
    myList = []
    for i in list:
        i = function(i)
        myList.append(i)
    return myList


print(map((lambda x: x + 1), [1, 3, 5, 7]))


def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result


print(foldl((lambda x, y: x // y), [2, 5], 5))


def foldr(function, list, initial):
    result = initial
    list.reverse()
    for item in list:
        result = function(item, result)
    return result


def reverse(list):
    list.reverse()
    return list
