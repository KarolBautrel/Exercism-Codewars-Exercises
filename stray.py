def stray(arr):
    myList = []
    for i in arr:
        if arr.count(i) == 1:
            print(i)


stray([3, 2, 2, 2, 2])
