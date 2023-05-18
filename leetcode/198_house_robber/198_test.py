import unittest
from house_robber import Solution
from common.binary_tree import *


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([1, 2, 3, 1],
                  4))
    cases.append(([2, 7, 9, 3, 1],
                  12))
    cases.append(([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177,
                   235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211],
                  3365))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().rob(case))


if __name__ == '__main__':
    unittest.main()
