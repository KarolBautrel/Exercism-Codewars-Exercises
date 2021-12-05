
def largest(min_factor, max_factor):
    mylist = []
    for first_num in range(min_factor, max_factor+1):
        for second_num in range(min_factor, max_factor+1):
            item = first_num*second_num
            if str(item) == str(item)[::-1]:
                mylist.append(item)
    return(max(mylist))


def smallest(min_factor, max_factor):
    mylist = []
    for first_num in range(min_factor, max_factor+1):
        for second_num in range(min_factor, max_factor+1):
            item = first_num*second_num
            if str(item) == str(item)[::-1]:
                mylist.append(item)
    return(min(mylist))
