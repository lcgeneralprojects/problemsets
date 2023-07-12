import unittest
from pacific_atlantic_water_flow import Solution
from common.binary_tree import *


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
                  [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]))
    cases.append(([[1]],
                  [[0, 0]]))
    cases.append(([[2, 1], [1, 2]],
                  [[0, 0], [0, 1], [1, 0], [1, 1]]))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().pacificAtlantic(case))


if __name__ == '__main__':
    unittest.main()
