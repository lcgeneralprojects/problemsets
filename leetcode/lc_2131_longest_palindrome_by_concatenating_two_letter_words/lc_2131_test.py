import unittest
from lc_f_2131_longest_palindrome_by_concatenating_two_letter_words import Solution


class MyTests(unittest.TestCase):

    # Cases are submitted in the format (input, expected_output
    cases = list()
    cases.append((["lc","cl","gg"],
                 6))
    cases.append((["ab","ty","yt","lc","cl","ab"],
                  8))
    cases.append((["cc","ll","xx"],
                  2))
    cases.append((["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"],
                  22))
    cases.append((["mm","mm","yb","by","bb","bm","ym","mb","yb","by","mb","mb","bb","yb","by","bb","yb","my","mb","ym"],
                  30))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().longestPalindrome(case))

if __name__ == '__main__':
    unittest.main()