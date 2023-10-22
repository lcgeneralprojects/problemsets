import unittest
from lc_f_7_reverse_integer import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((123,
                  321))
    cases.append((-123,
                  -321))
    cases.append((120,
                  21))
    cases.append((1534236469,
                  0))
    cases.append((-2147483412,
                  -2143847412))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().reverse(case))


if __name__ == '__main__':
    unittest.main()
