from preprocess import remove_spaces, pretty_comma, pretty_slash, pretty_dot
from words import Word
s = '"""****Московская область , г.БАЛАШИХА ,        Маяковского, дом 16  \\  344, корп. а  .'


def dragon_algo(s):
    s = pretty_dot(s)
    s = remove_spaces(s)
    s = pretty_comma(s)
    s = pretty_slash(s)

    print(s)

    word_group = []
    for k,w in enumerate(s.split()):
        if w == '':
            continue
        word = Word(k,w)
        word_group.append(word)



dragon_algo(s)