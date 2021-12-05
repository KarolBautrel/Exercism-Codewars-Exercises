def run_length_encoding(seq):
    compressed = []
    count = 1
    char = seq[0]
    for i in range(1, len(seq)):
        if seq[i] == char:
            count = count + 1
        else:
            new = str(char), str(count)
            compressed.append(new)
            char = seq[i]
            count = 1
        l = compressed.strip([])
        print(l)


print(run_length_encoding("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"))
