import unittest
from lc_24_f_swap_nodes_in_pairs import Solution
from lc_common.lc_singly_linked_list import listToSLL, SLLToList


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((listToSLL([1,2,3,4]),
                  [2,1,4,3]))
    cases.append((listToSLL([]),
                  []))
    cases.append((listToSLL([1]),
                  [1]))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, SLLToList(Solution().swapPairs(case)))


if __name__ == '__main__':
    unittest.main()
