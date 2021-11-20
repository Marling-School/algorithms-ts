from typing import List, Union

StrOrInt = Union[str, int]


def quick_sort(input_list: List[StrOrInt]) -> List[StrOrInt]:
    """"
    Sorts the input list, using the provided comparator
    to decide if two elements are in the correct order.
    Returns a copy of the list sorted, makes no changes to input list.
    This function delegates to the recursive form, initialising the left and right pointers.
    """

    # Make a copy of the list, so that the original remains untouched
    output_list = list(input_list)
    print(output_list)

    if len(input_list) < 2:
        return output_list

    return quick_sort_recurse(output_list, 0, len(input_list) - 1)


def quick_sort_recurse(arr: List[StrOrInt],
                       left_pointer: int,
                       right_pointer: int) -> List[StrOrInt]:
    """"
    Recursive form of the quick sort that requires the left and right pointers.
    """
    if left_pointer < right_pointer:
        # pi is partitioning index, input_list[pi] is now at right place
        pi: int = partition(arr, left_pointer, right_pointer)

        quick_sort_recurse(arr, left_pointer, pi - 1)  # Before pi
        quick_sort_recurse(arr, pi + 1, right_pointer)  # After pi

    return arr


def partition(arr: List[StrOrInt],
              left_pointer: int,
              right_pointer: int):
    """
        This function takes last element as pivot, places
        the pivot element at its correct position in sorted
        input_listay, and places all smaller (smaller than pivot)
        to left of pivot and all greater elements to right
        of pivot
    """

    # pivot (Element to be placed at right position)
    pivot: StrOrInt = arr[right_pointer]

    i: int = left_pointer - 1  # Index of smaller element

    for j in range(left_pointer, right_pointer):  # rightPointer - 1?
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            i += 1  # increment index of smaller element
            swap = arr[i]
            arr[i] = arr[j]
            arr[j] = swap

    # Put the pivot in its place
    swap = arr[i + 1]
    arr[i + 1] = arr[right_pointer]
    arr[right_pointer] = swap

    return i + 1
