import unittest
from lc_f_347_top_k_frequent_elements import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((([1, 1, 1, 2, 2, 3], 2),
                  [1, 2]))
    cases.append((([1], 1),
                  [1]))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().topKFrequent(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
