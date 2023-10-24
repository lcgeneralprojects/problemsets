import unittest
from lc_515_f_find_largest_value_in_each_tree_row import Solution
from lc_common.lc_binary_tree import TreeNode,


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([1, 3, 2, 5, 3, 'null', 9],
                  [1, 3, 9]))
    cases.append(([1, 2, 3],
                  [1, 3]))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().largestValues(case))


if __name__ == '__main__':
    unittest.main()
