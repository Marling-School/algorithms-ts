from typing import List, Optional
from random import randint
from quick_sort import quick_sort


def test_numbers():
    my_list: List[int] = [4, 5, 3, 1, 9, 8]
    my_sorted_list: List[int] = quick_sort(my_list)
    assert [1, 3, 4, 5, 8, 9] == my_sorted_list


def test_empty_list():
    my_list: List = []
    sorted_list = quick_sort(my_list)
    assert [] == sorted_list


def test_string():
    my_list: List[str] = ["Bravo", "Delta", "Charlie",
                          "Alpha", "Echo", "Sierra", "Foxtrot"]
    my_sorted_list: List[str] = quick_sort(my_list)
    assert ["Alpha", "Bravo", "Charlie", "Delta",
            "Echo", "Foxtrot", "Sierra"] == my_sorted_list


def test_random():
    my_list: List[int] = [randint(0, 100) for i in range(100)]
    my_sorted_list: List[int] = quick_sort(my_list)

    last: Optional[int] = None
    num_checks: int = 0
    for s in my_sorted_list:
        if last is not None:
            num_checks += 1
            assert last <= s
        last = s
    assert num_checks == len(my_list) - 1
