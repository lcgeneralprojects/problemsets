import unittest
from lc_f_10_regular_expression_matching import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((['aa', 'a'],
                  False))
    cases.append((['aa', 'a*'],
                  True))
    cases.append((['ab', '.*'],
                  True))
    cases.append((['aab', 'c*a*b'],
                  True))
    cases.append((['mississippi', 'mis*is*ip*.'],
                  True))
    cases.append((['mississippi', 'mis*is*p*.'],
                  False))
    cases.append((['bbbba', '.*a*a'],
                  True))
    cases.append((['aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*c'],
                  False))
    cases.append((['cbaacacaaccbaabcb', 'c*b*b*.*ac*.*bc*a*'],
                  True))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().isMatch(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
