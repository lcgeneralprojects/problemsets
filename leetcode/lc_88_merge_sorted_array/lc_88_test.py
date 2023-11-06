import unittest
from lc_88_f_merge_sorted_array import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
                  [1, 2, 2, 3, 5, 6]))
    cases.append(([[1], 1, [], 0],
                  [1]))
    cases.append(([[0], 0, [1], 1],
                  [1]))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().merge(*case))


if __name__ == '__main__':
    unittest.main()
