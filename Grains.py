
def square(number):
    if number not in range(1, 65):
        raise ValueError(
            "Squares on chessboard must be integers between 1 and 64.")

    else:
        chessBoard = [0]
        i = 1
        while len(chessBoard) < 65:
            chessBoard.append(i)
            i *= 2
        return chessBoard[number]


def total():
    return 2**64 - 1
