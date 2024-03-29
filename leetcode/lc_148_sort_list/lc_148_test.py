import unittest
from lc_f_148_sort_list import Solution
from common.singly_linked_list import *


class MyTests(unittest.TestCase):

    # Cases are submitted in the format (input, expected_output
    cases = list()
    # cases.append((listToSLL([4,2,1,3]), [1,2,3,4]))
    # cases.append((listToSLL([-1,5,3,4,0]), [-1,0,3,4,5]))
    cases.append((stringToSLL([]), []))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, SLLToString(Solution().sortList(case)))


if __name__ == '__main__':
    unittest.main()
