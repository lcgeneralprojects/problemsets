import unittest
from lc_25_f_reverse_nodes_in_k_group import Solution
from lc_common.lc_singly_linked_list import listToSLL, SLLToList


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([listToSLL([1, 2, 3, 4, 5]), 2],
                  [2, 1, 4, 3]))
    cases.append((listToSLL([]),
                  []))
    cases.append((listToSLL([1]),
                  [1]))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, SLLToList(Solution().reverseKGroup(case[0], case[1])))


if __name__ == '__main__':
    unittest.main()
