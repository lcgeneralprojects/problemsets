import unittest
from path_sum_III import Solution
from common.binary_tree import *


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(((dequeToTree(deque([10, 5, -3, 3, 2, 'null', 11, 3, -2, 'null', 1])), 8),
                  3))
    cases.append(((dequeToTree(deque([5, 4, 8, 11, 'null', 13, 4, 7, 2, 'null', 'null', 5, 1])), 22),
                  3))
    cases.append(((dequeToTree(deque([1])), 0),
                  0))
    cases.append(((dequeToTree(deque([-2, 'null', -3])), -3),
                  1))
    cases.append(((dequeToTree(deque([-2,'null',-3])), -5),
                  1))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().pathSum(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
