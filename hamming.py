def distance(strand_a, strand_b):

    if len(strand_a) == len(strand_b):
        i = 0
        for a, b in zip(strand_a, strand_b):
            if a != b:
                i += 1
        return i
    else:
        raise ValueError("Strands must be of equal length.")


print(distance('cad', 'b'))
