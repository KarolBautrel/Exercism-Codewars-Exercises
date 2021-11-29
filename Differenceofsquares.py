def square_of_sum(number):
    listofNumber = []
    for i in range(0, number+1):
        listofNumber.append(i)

    return (sum(listofNumber))**2


print(square_of_sum(10))


def sum_of_squares(number):
    listofNumber = []
    listofSquares = []
    for i in range(0, number+1):
        listofNumber.append(i)
    for i in listofNumber:
        i = i**2
        listofSquares.append(i)
    return (sum(listofSquares))


print(sum_of_squares(10))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)


print(difference_of_squares(10))
