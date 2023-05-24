import unittest
from zigzag_conversion import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((("PAYPALISHIRING", 3),
                  "PAHNAPLSIIGYIR"))
    cases.append((("PAYPALISHIRING", 4),
                  "PINALSIGYAHRPI"))
    cases.append((("A", 1),
                  "A"))
    cases.append((("AB", 1),
                  "AB"))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().convert(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
