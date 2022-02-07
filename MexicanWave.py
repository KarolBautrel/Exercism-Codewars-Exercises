def wave(people):
    myList = []
    for i in range(len(people)):
        if people[i] != " ":
            var = people[:i].lower() + people[i:].capitalize()
            myList.append(var)
    return myList


var = "two words"
print(wave(var))
for i in range(len(var)):
    print(var[:i].lower()+var[i:].capitalize())
