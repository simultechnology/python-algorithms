import unittest

import algorithms.sort as sort


class SearchTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_selectionSort(self):
        items = [5, 3, 6, 2, 10, 32, 4, 21, 9, 11]
        item = sort.selectionSort(items)
        self.assertEqual(item, [2, 3, 4, 5, 6, 9, 10, 11, 21, 32])


if __name__ == '__main__':
    unittest.main()
