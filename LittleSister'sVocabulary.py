def add_prefix_un(string):
    return "un"+string


print(add_prefix_un("happy"))


def make_word_groups(vocab_words):
    return vocab_words[0] + " :: " + " :: ".join([vocab_words[0]+s for s in vocab_words[1:]])


'''
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    return prefix + " :: " + " :: ".join([prefix+s for s in vocab_words[1:]])

'''
print(make_word_groups(['en', 'circle', 'fold', 'close',
      'joy', 'lighten', 'tangle', 'able', 'code', 'culture']))


def remove_suffix_ness(string):
    if string[-5] == "i":
        return string[:-5] + "y"
    else:
        return string[:-4]


print(remove_suffix_ness("sadness"))


def noun_to_verb(sentence, index):
    withoutDot = sentence.replace(".", "")
    l = list(withoutDot.split())
    return l[index] + "en"


print(noun_to_verb('I need to make that bright.', -1))
