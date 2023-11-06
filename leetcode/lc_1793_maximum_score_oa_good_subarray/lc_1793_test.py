import unittest
from lc_1793_f_maximum_score_of_a_good_subarray import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([[1, 4, 3, 7, 4, 5], 3],
                  15))
    cases.append(([[5, 5, 4, 5, 4, 1, 1, 1], 0],
                  20))
    cases.append(([[6569, 9667, 3148, 7698, 1622, 2194, 793, 9041, 1670, 1872], 5],
                  9732))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().maximumScore(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
