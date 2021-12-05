"""Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times."""


list = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]


def find_it(seq):
    return [i for i in seq if (len(i) % 2) == 1]


print(find_it(list))
