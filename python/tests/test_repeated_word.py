from code_challenges.hashmap_repeated_word.repeated_word import repeated_word


def test_repeat():
    str = "Once upon a time, there was a brave princess who..."
    assert repeated_word(str) == "a"



def test_repeat_2():
    str = "Tell me lies, tell me sweet little lies Tell me lies Tell me, tell me lies"
    assert repeated_word(str) == 'tell'

def test_repate_3():
    str = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didnt know what I was doing in New York...'
    assert repeated_word(str) == 'was'
