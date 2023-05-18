import unittest
from coin_change import Solution
from common.binary_tree import *


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((([1, 2, 5], 11),
                  3))
    cases.append((([2], 3),
                  -1))
    cases.append((([1], 0),
                  0))
    cases.append((([474, 83, 404, 3], 264),
                  8))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().coinChange(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
