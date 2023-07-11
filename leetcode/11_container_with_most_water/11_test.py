import unittest
from container_with_most_water import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append(([1, 8, 6, 2, 5, 4, 8, 3, 7],
                  49))
    cases.append(([1, 1],
                  1))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().maxArea(case))


if __name__ == '__main__':
    unittest.main()
