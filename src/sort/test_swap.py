from src.sort.swap import swap


def test_swap():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    swap(my_list, 2, 3)
    assert my_list[2] == 4
    assert my_list[3] == 3
