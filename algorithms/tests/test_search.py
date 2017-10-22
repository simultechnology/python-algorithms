import unittest

import algorithms.search as search


class SearchTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_binary_search(self):
        items = list(range(1, 256, 2))
        print(len(items))
        item = search.binary_search(items, 111)
        self.assertEqual(item, 55)


if __name__ == '__main__':
    unittest.main()
