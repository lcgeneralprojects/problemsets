import unittest
from lc_23_f_merge_k_sorted_lists import Solution
from lc_common.lc_singly_linked_list import listToSLL, SLLToList


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([listToSLL([1, 4, 5]), listToSLL([1, 3, 4]), listToSLL([2, 6])],
                  [1, 1, 2, 3, 4, 4, 5, 6]))
    cases.append(([],
                  []))
    cases.append(([listToSLL([])],
                  []))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, SLLToList(Solution().mergeKLists(case)))


if __name__ == '__main__':
    unittest.main()
