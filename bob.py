def response(hey_bob=None):
    if hey_bob.isupper() and hey_bob[-1] == "?":
        return '''Calm down, I know what I'm doing!'''
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    elif hey_bob.isspace() or hey_bob == "":
        return 'Fine. Be that way!'

    elif hey_bob.strip()[-1] == "?":
        return 'Sure.'

    else:
        return 'Whatever.'


print(response(""))
