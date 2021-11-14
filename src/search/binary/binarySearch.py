from typing import List
from math import floor

NO_MATCH = -1


def binarySearch(items: List[str], item: str) -> int:
    # Calculate initial values of lowest/highest pointers to encapsulate whole list
    lowest_ptr: int = 0
    highest_ptr: int = len(items) - 1

    while True:
        # Calculate new middle and make the comparison
        middle_ptr: int = floor((lowest_ptr + highest_ptr) / 2)

        if item == items[middle_ptr]:
            # Item found, return its index
            return middle_ptr
        elif lowest_ptr == highest_ptr:
            # This is the exit condition, we haven't found what we are looking for
            return NO_MATCH
        elif item < items[middle_ptr]:
            # If the item is smaller than the middle, look in the lower half
            if middle_ptr == 0:
                return NO_MATCH
            highest_ptr = middle_ptr - 1
        else:
            # The item must be larger than the middle, look in the upper half
            if middle_ptr == len(items) - 1:
                return NO_MATCH
            lowest_ptr = middle_ptr + 1
