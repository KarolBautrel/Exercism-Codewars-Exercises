def to_rna(dna_strand):
    rnaList = list(dna_strand)
    for i in range(len(rnaList)):
        if rnaList[i] == "G":
            rnaList[i] = "C"
        elif rnaList[i] == "C":
            rnaList[i] = "G"
        elif rnaList[i] == "T":
            rnaList[i] = "A"
        elif rnaList[i] == "A":
            rnaList[i] = "U"
        else:
            return ""
    return [i for i in rnaList]


print(to_rna("G"))


def to_rna(dna_strand):
    rnaList = list(dna_strand)
    myList = []

    for i in rnaList:
        if i == "G":
            myList.append("C")
        elif i == "C":
            myList.append("G")
        elif i == "T":
            myList.append("A")
        elif i == "A":
            myList.append("U")
        else:
            return ""
    return ''.join([i for i in myList])


print(to_rna("ACGTGGTCTTAA"))
