import unittest
from lc_29_f_divide_two_integers import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([10, 3],
                  3))
    cases.append(([7, -3],
                  -2))
    cases.append(([-2147483648, 1],
                  -2147483648))

    def test_something(self):
        for case, expected in self.cases:
            # If there is a single argument in the input, case should not be treated as a list,
            # and 'case[0], case[1]' should be reduced to 'case' in such situations
            self.assertEqual(expected, Solution().divide(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
