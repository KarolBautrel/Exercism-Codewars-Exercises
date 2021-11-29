"""In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out."""

list = [1, 2, 'a', 'b']


def filter_list(listint):
    return [i for i in listint if isinstance(i, int)]


print(filter_list(list))


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
