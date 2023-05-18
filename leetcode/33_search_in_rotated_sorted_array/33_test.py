import unittest
from search_in_rotated_sorted_array import Solution
from common.binary_tree import *


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((([4, 5, 6, 7, 0, 1, 2], 0),
                  4))
    cases.append((([4, 5, 6, 7, 0, 1, 2], 3),
                  -1))
    cases.append((([1], 0),
                  -1))
    cases.append((([5, 1, 3], 1),
                  1))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().search(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
