def capitalize_title(title):
    return title.title()


print(capitalize_title("jestem fajnym chlopcem"))


def check_sentence_ending(sentence):
    if sentence[-1] == ".":
        return True
    else:
        return False


def clean_up_spacing(sentence):
    return sentence.strip()


def replace_word_choice(sentece, changed, changer):
    return sentece.replace(changed, changer)
