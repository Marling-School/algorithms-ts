import unittest

from binarySearch import binarySearch, NO_MATCH


class TestBinarySearch(unittest.TestCase):

    def test_strings(self):
        myList = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo',
                  'Foxtrot', 'Golf', 'Hotel', 'Juliet', 'Kilo', 'Lima']
        # Normal data which is in the list
        charlie = binarySearch(myList, 'Charlie')
        self.assertEqual(charlie, 2)

        # Edge cases
        alpha = binarySearch(myList, 'Alpha')
        self.assertEqual(alpha, 0)

        lima = binarySearch(myList, 'Lima')
        self.assertEqual(lima, 10)

        # Not found
        bob = binarySearch(myList, 'bob')
        self.assertEqual(bob, NO_MATCH)


if __name__ == '__main__':
    unittest.main()
