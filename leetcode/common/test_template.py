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
            self.assertEqual(expected, Solution().METHOD(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
