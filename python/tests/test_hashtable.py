from hashtable.hashtable import Hashtable

def test_succesful_import():
    assert Hashtable


def test_table():
    hashtable = Hashtable()
    assert hashtable.hash('Olive') == 415

def test_addition():
    hashtable =Hashtable()
    hashtable.add('Olive',2)
    assert hashtable.bucket[415] == [('Olive',2)]
