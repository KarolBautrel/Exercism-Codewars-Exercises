def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active and touching_ghost:
        return True
    else:
        return False


def score(touching_power_pellet, touching_dot):
    if touching_power_pellet or touching_dot:
        return True
    else:
        return False


def lose(power_pellet_active, touching_ghost):
    if power_pellet_active and touching_ghost:
        return False
    if touching_ghost == False:
        return False
    else:
        return True


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if touching_ghost == False:
        return True

    elif power_pellet_active and has_eaten_all_dots and touching_ghost:
        return True
    elif power_pellet_active and has_eaten_all_dots == True and touching_ghost == False:
        return True
    elif power_pellet_active and has_eaten_all_dots == True:
        return True
    elif has_eaten_all_dots and touching_ghost == True:
        return False
    elif has_eaten_all_dots == True:
        return True
    else:
        return False


print(win(False, False, True))
