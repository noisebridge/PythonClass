import enchant


en_dict = enchant.Dict('en_US')

def is_word(word):
    return en_dict.check(word)
