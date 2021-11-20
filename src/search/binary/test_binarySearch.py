import unittest

from binary_search import binarySearch, NO_MATCH


def test_strings():
    myList = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo',
              'Foxtrot', 'Golf', 'Hotel', 'Juliet', 'Kilo', 'Lima']
    # Normal data which is in the list
    charlie = binarySearch(myList, 'Charlie')
    assert charlie == 2

    # Edge cases
    alpha = binarySearch(myList, 'Alpha')
    assert alpha == 0

    lima = binarySearch(myList, 'Lima')
    assert lima == 10

    # Not found
    bob = binarySearch(myList, 'bob')
    assert bob == NO_MATCH
