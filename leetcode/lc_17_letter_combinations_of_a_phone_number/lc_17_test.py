import unittest
from lc_17_letter_combinations_of_a_phone_number.lc_17_letter_combinations_of_a_phone_number import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((['23'],
                  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]))
    cases.append(([''],
                  []))
    cases.append((['2'],
                  ["a", "b", "c"]))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().letterCombinations(case[0]))


if __name__ == '__main__':
    unittest.main()
