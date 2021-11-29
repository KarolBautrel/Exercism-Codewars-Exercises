def abbreviate(words):
    wordsWithoutBlankSpaces = words.strip()
    wordsWithoutChar = wordsWithoutBlankSpaces.replace(
        '-', ' ').replace('_', ' ')
    wordsList = wordsWithoutChar.split()
    print(wordsList)
    acronymlist = []
    for elements in wordsList:
        acronymlist.append(elements[0])
    acronym = ''.join(acronymlist)

    return acronym.upper()


print(abbreviate("The Road _Not_ Taken"))
