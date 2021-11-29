def find_anagrams(word, candidates):
    anagrams = []

    for i in candidates:
        if sorted(i.upper()) == sorted(word.upper()):
            anagrams.append(i)
    print(anagrams)
    for i in candidates:
        if i.upper() == word:
            anagrams.remove(i)
    return anagrams


candidates = ["BANANA", "Banana", "banana"]
print(find_anagrams("BANANA", candidates))
