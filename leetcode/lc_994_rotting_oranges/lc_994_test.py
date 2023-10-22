import unittest
from lc_f_994_rotting_oranges import Solution
from common.binary_tree import *


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([[2, 1, 1], [1, 1, 0], [0, 1, 1]],
                  4))
    cases.append(([[2, 1, 1], [0, 1, 1], [1, 0, 1]],
                  -1))
    cases.append(([[0, 2]],
                  0))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().orangesRotting(case))


if __name__ == '__main__':
    unittest.main()
