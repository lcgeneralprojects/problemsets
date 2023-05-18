import unittest
from search_a_2D_matrix import Solution
from common.binary_tree import *


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),
                  True))
    cases.append((([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13),
                  False))
    cases.append((([[1]], 2),
                  False))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().searchMatrix(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
