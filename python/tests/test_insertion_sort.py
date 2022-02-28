from code_challenges.insertion_sort.insertion_sort import insertion_sort

def test_import():
    assert insertion_sort
def test_insertion_sort():
    list = [8,6,7,5,3,2,9]
    assert insertion_sort(list) == [2,3,5,6,7,8,9]
