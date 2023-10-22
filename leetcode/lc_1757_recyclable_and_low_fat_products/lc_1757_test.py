import unittest
from MAIN_FILE import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(('INPUT',
                  'EXPECTED OUTPUT'))
    cases.append(('INPUT',
                  'EXPECTED OUTPUT'))
    cases.append(('INPUT',
                  'EXPECTED OUTPUT'))
    cases.append(('INPUT',
                  'EXPECTED OUTPUT'))

    def test_something(self):
        for case, expected in self.cases:
            # If there is a single argument in the input, case should not be treated as a list,
            # and 'case[0], case[1]' should be reduced to 'case' in such situations
            self.assertEqual(expected, Solution().METHOD(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
