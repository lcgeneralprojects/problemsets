import unittest
from lc_f_12_integer_to_roman import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((3,
                  "III"))
    cases.append((58,
                  "LVIII"))
    cases.append((1994,
                  "MCMXCIV"))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().intToRoman(case))


if __name__ == '__main__':
    unittest.main()
