import unittest
from lc_22_f_generate_parentheses import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((3,
                  ["((()))", "(()())", "(())()", "()(())", "()()()"]))
    cases.append((1,
                  ["()"]))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().generateParentheses(case))


if __name__ == '__main__':
    unittest.main()
