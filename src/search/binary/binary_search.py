from typing import List, Union
from math import floor

NO_MATCH = -1

StrOrInt = Union[str, int]


def binarySearch(items: List[StrOrInt], itemToFind: StrOrInt) -> int:
    """
        Search for an item in a list.
        When it finds the item, it returns the index of that item.
        If the item cannot be found, it will return -1
    """
    result: int = None

    # Calculate initial values of lowest/highest pointers to encapsulate whole list
    lowest_ptr: int = 0
    highest_ptr: int = len(items) - 1

    while result == None:
        # Calculate new middle and make the comparison
        middle_ptr: int = floor((lowest_ptr + highest_ptr) / 2)

        if itemToFind == items[middle_ptr]:
            # Item found, return its index
            result = middle_ptr
        elif lowest_ptr == highest_ptr:
            # This is the exit condition, we haven't found what we are looking for
            result = NO_MATCH
        elif itemToFind < items[middle_ptr]:
            # If the item is smaller than the middle, look in the lower half
            if middle_ptr == 0:
                result = NO_MATCH
            highest_ptr = middle_ptr - 1
        elif itemToFind > items[middle_ptr]:
            # The item is larger than the middle, look in the upper half
            if middle_ptr == len(items) - 1:
                result = NO_MATCH
            lowest_ptr = middle_ptr + 1

    return result
