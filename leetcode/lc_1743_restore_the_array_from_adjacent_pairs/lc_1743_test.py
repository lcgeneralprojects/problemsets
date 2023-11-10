import unittest
from lc_1743_f_restore_the_array_from_adjacent_pairs import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([[[2, 1], [3, 4], [3, 2]]],
                  [1, 2, 3, 4]))
    cases.append(([[[4, -2], [1, 4], [-3, 1]]],
                  [-2, 4, 1, -3]))
    cases.append(([[[100000, -100000]]],
                  [100000, -100000]))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().restoreArray(*case))


if __name__ == '__main__':
    unittest.main()
