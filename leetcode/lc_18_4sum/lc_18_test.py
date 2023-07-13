import unittest
from lc_18_4sum.lc_18_4sum import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([[1, 0, -1, 0, -2, 2], 0],
                  [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]))
    cases.append(([[2, 2, 2, 2, 2], 8],
                  [[2, 2, 2, 2]]))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().fourSum(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
