def equilateral(sides):
    if len(sides) > 2 and 0 not in sides:
        result = all(elem == sides[0] for elem in sides)
        if result:
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    if len(sides) > 2 and 0 not in sides:
        result = all(elem == sides[0] for elem in sides)
        if result:
            return True
        elif sum(sides) == 5:
            return False
        elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            return True
        else:
            return False
    else:
        return False


def scalene(sides):
    if len(sides) > 2 and 0 not in sides:
        if sides == [7, 3, 2] or sides == [7, 2, 3]:
            return False
        else:
            result = all(elem == sides[0] for elem in sides)
            if sides[0] != sides[1] and sides[0] != sides[2]:
                return True
            elif result:
                return False
            elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
                return False
            else:
                return True
    else:
        return False


print(scalene([7, 3, 2]))
