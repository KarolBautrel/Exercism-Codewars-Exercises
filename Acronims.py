def abbreviate(words):
    words.replace('-', ' ').replace('_', ' ')
    wordsList = words.split()
    acronymlist = []
    for elements in wordsList:
        acronymlist.append(elements[0])
    acronymString = ''.join(acronymlist)
    acronymWithoutBlankSpaces = acronymString.strip()
    acronym = acronymWithoutBlankSpaces.replace(
        '-', ' ').replace('_', ' ')
    print(acronymString)

    return acronym.upper()


print(abbreviate("Complementary metal-oxide semiconductor"))


dupa = ("Complementary metal-oxide semiconductor")

print(dupa.replace('-', ' '))
