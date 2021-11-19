from typing import List, Union
from math import floor

NO_MATCH = -1

StrOrInt = Union[str, int]


def linearSearch(items: List[StrOrInt],
                 itemToFind: StrOrInt) -> int:
    """
    Searches through a list by comparing every item to the criteria.
    """
    for index, item in enumerate(items):
        if item == itemToFind:
            return index

    return NO_MATCH
