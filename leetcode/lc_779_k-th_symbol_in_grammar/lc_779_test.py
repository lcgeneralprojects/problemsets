import unittest
from lc_779_f_k_th_symbol_in_grammar import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([1, 1],
                  0))
    cases.append(([2, 1],
                  0))
    cases.append(([2, 2],
                  1))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().kthGrammar(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
