import unittest
from lc_35_f_search_insert_position import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([[1, 3, 5, 6], 5],
                  2))
    cases.append(([[1, 3, 5, 6], 2],
                  1))
    cases.append(([[1, 3, 5, 6], 7],
                  4))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().searchInsert(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
