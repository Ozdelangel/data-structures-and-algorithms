from code_challenges.quick_sort.quick_sort import quick_sort


def test_import():
    assert quick_sort

def test_first_list():
    list = [8,4,23,42,16,15]
    quick_sort(list,0,len(list) - 1)
    assert list == [4,8,15,16,23,42]

def test_reverse_sorted():
    list = [20,18,12,8,5,-2]
    quick_sort(list,0,len(list) - 1)
    assert list == [-2,5,8,12,18,20]

def test_few_uniques():
    list = [5,12,7,5,5,7]
    quick_sort(list,0,len(list) - 1)
    assert list == [5,5,5,7,7,12]

def test_nearly_sorted():
    list = [2,3,5,7,13,11]
    quick_sort(list,0,len(list) - 1)
    assert list == [2,3,5,7,11,13]

