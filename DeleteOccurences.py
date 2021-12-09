
"""Task
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering.
 For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
 drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times,
  and then take 3, which leads to [1,2,3,1,2,3]."""


def delete_nth(order, max_e):
    if not order or max_e < 1:
        return []

    counted_order = {x: 0 for x in order}
    print(counted_order)
    print(counted_order[7])
    new_order = []

    for item in order:
        if counted_order[item] < max_e:
            counted_order[item] += 1
            new_order.append(item)

    return new_order


print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
