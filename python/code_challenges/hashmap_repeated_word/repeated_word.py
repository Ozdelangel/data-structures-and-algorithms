from collections import Counter

def repeated_word(str):
    sentence = str.lower().split(' ')
    rep_word = Counter(sentence)


    for key in sentence:
        if rep_word[key] > 1:

            return key
