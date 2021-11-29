def get_rounds(number):
    endround = number + 3
    numberList = []
    while number < endround:
        numberList.append(number)
        number += 1
    return numberList


def concatenate_rounds(rounds_1, rounds_2):
    return (rounds_1 + rounds_2)


print(concatenate_rounds([27, 28, 29], [35, 36]))


def list_contains_round(rounds, number):
    if number in rounds:
        return True
    else:
        return False


print(list_contains_round([27, 28, 29, 35, 36], 30))


def card_average(hand):
    return sum(hand)/len(hand)


list = [1, 2, 3, 4]
average = sum(list)/len(list)
print(average)


def approx_average_is_average(hand):
    average = sum(hand)/len(hand)
    if average == len(hand):
        return True
    elif average in hand:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    average = sum(hand)/len(hand)
    if average == len(hand):
        return True
    elif average in hand:
        return True
    else:
        return False


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand.pop()
        hand.append(22)
        return hand
    else:
        return hand


print(maybe_double_last([5, 9, 10]))
