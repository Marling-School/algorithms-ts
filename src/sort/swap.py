from typing import List


def swap(arr: List, i: int, j: int):
    """
    Given a list, it swaps the items at i and j
    """
    s = arr[i]
    arr[i] = arr[j]
    arr[j] = s
