import unittest
from lc_342_f_power_of_four import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((16,
                  True))
    cases.append((5,
                  False))
    cases.append((1,
                  True))
    cases.append((99,
                  False))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().isPowerOfFour(case))


if __name__ == '__main__':
    unittest.main()
