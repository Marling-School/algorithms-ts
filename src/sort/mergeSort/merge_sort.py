from typing import List, Union
from math import floor
StrOrInt = Union[str, int]


def merge_sort(input_list: List[StrOrInt]) -> List[StrOrInt]:
    if len(input_list) == 0:
        return list(input_list)

    """"
    Sorts the input list
    Returns a copy of the list sorted, makes no changes to input list.
    This function delegates to the recursive form, initialising the left and right pointers.
    """
    return merge_sort_recurse(input_list, 0, len(input_list) - 1)


def merge_sort_recurse(input_list: List[StrOrInt],
                       left_pointer: int,
                       right_pointer: int) -> List[StrOrInt]:
    """"
    Recursive form of the merge sort that requires the left and right pointers.
    """
    # Exit condition, the list is a single item
    if left_pointer == right_pointer:
        return [input_list[left_pointer]]

    # Calculate the mid point
    middle: int = floor((left_pointer + right_pointer) / 2)

    # Recurse sort both halves to yield two lists to merge
    first_half: List[StrOrInt] = merge_sort_recurse(
        input_list, left_pointer, middle)
    second_half: List[StrOrInt] = merge_sort_recurse(
        input_list, middle + 1, right_pointer)

    # Merge the two halves into a single sorted list
    output_list: List[StrOrInt] = []
    while (len(first_half) > 0) and (len(second_half) > 0):
        # If the item in the 'first half' is larger than the second half
        if first_half[0] > second_half[0]:
            output_list.append(second_half.pop(0))
        else:
            output_list.append(first_half.pop(0))

    # Push any stragglers from whichever list has items remaining
    output_list.extend(first_half)
    output_list.extend(second_half)

    return output_list
