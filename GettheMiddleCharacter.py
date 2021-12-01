def get_middle(s):
    if (len(s) % 2) == 0:
        middleStr = len(s)/2
        print(middleStr)
        return s[int(middleStr-1)] + s[int(middleStr)]
    if (len(s) % 2) == 1:
        middleStr = len(s)/2
        print(int(middleStr))
        return s[int(middleStr)]
