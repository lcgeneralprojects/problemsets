import unittest
from lc_844_f_backspace_string_compare import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((['ab#c', 'ad#c'],
                  True))
    cases.append((['ab##', 'c#d#'],
                  True))
    cases.append((['a#c', 'b'],
                  False))

    def test_something(self):
        for case, expected in self.cases:
            # If there is a single argument in the input, case should not be treated as a list,
            # and 'case[0], case[1]' should be reduced to 'case' in such situations
            self.assertEqual(expected, Solution().backspaceCompare(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
