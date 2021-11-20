from typing import List, Union

StrOrInt = Union[str, int]


def insertion_sort(input_list: List[StrOrInt]) -> List[StrOrInt]:
    """"
    Sorts the input list
    Returns a copy of the list sorted, makes no changes to input list
    """
    output_list: List[StrOrInt] = list(input_list)

    for index in range(1, len(output_list)):
        item_to_place: StrOrInt = output_list[index]
        item_place: int = index

        while item_place > 0:
            lower: int = item_place - 1
            upper: int = item_place

            # The comparator returns -1 if the first item is 'greater than' the second one
            if output_list[lower] > item_to_place:
                # Temporary variable to prevent overwrites
                swap: StrOrInt = output_list[lower]
                output_list[lower] = output_list[upper]
                output_list[upper] = swap
            else:
                # Item to place can be placed early
                item_place = upper
                break
            item_place -= 1

        output_list[item_place] = item_to_place

    return output_list
