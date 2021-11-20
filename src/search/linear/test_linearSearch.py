from linear_search import linearSearch, NO_MATCH


def test_strings():
    myList = ['Hotel', 'Alpha', 'Kilo', 'Charlie', 'Echo',
              'Foxtrot', 'Delta', 'Juliet', 'Lima', 'Golf', 'Bravo']
    # Normal data which is in the list
    charlie = linearSearch(myList, 'Charlie')
    assert charlie == 3

    # Edge cases
    alpha = linearSearch(myList, 'Alpha')
    assert alpha == 1

    lima = linearSearch(myList, 'Lima')
    assert lima == 8

    # Not found
    bob = linearSearch(myList, 'bob')
    assert bob == NO_MATCH
