import unittest

from linearSearch import linearSearch, NO_MATCH


class TestLinearSearch(unittest.TestCase):

    def test_strings(self):
        myList = ['Hotel', 'Alpha', 'Kilo', 'Charlie', 'Echo',
                  'Foxtrot', 'Delta', 'Juliet', 'Lima', 'Golf', 'Bravo']
        # Normal data which is in the list
        charlie = linearSearch(myList, 'Charlie')
        self.assertEqual(charlie, 3)

        # Edge cases
        alpha = linearSearch(myList, 'Alpha')
        self.assertEqual(alpha, 1)

        lima = linearSearch(myList, 'Lima')
        self.assertEqual(lima, 8)

        # Not found
        bob = linearSearch(myList, 'bob')
        self.assertEqual(bob, NO_MATCH)


if __name__ == '__main__':
    unittest.main()
