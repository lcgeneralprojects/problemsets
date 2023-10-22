import unittest
from lc_28_f_find_the_index_of_the_first_occurrence_in_a_string import Solution


class MyTests(unittest.TestCase):
    # Cases are submitted in the format (input, expected_output)
    cases = list()
    cases.append((["sadbutsad", "sad"],
                  0))
    cases.append((["leetcode", "leeto"],
                  -1))
    cases.append((["aaa", "aaaa"],
                  -1))

    def test_something(self):
        for case, expected in self.cases:
            # If there is a single argument in the input, case should not be treated as a list,
            # and 'case[0], case[1]' should be reduced to 'case' in such situations
            self.assertEqual(expected, Solution().strStr(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
