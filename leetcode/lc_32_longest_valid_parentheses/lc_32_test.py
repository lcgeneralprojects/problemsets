import unittest
from lc_32_f_longest_valid_parentheses import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(("(()",
                  2))
    cases.append((")()())",
                  4))
    cases.append(("",
                  0))
    cases.append(("()(()",
                  2))
    cases.append(("(())(",
                  4))

    def test_something(self):
        for case, expected in self.cases:
            # If there is a single argument in the input, case should not be treated as a list,
            # and 'case[0], case[1]' should be reduced to 'case' in such situations
            self.assertEqual(expected, Solution().longestValidParentheses(case))


if __name__ == '__main__':
    unittest.main()
