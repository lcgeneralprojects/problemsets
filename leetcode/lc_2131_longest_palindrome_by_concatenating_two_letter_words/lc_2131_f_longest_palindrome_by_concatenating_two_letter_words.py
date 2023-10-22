from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter(words)
        res = 0
        centre_flag = 0             # Taking into account a palindromic 2-letter string that
                                    # can be placed in the centre of the big palindrome

        for key in freq:

            if key[0] == key[1]:
                if centre_flag == 0 and freq[key] % 2 == 1:
                    centre_flag = 1
                    freq[key] -= 1
                    res += 2

                if freq[key] >= 2:
                    res += (freq[key] // 2) * 4
                    freq[key] = freq[key] % 2
            else:
                complementary_key = key[1]+key[0]
                # complementary_value = freq[complementary_key]
                if complementary_key in freq and freq[key] > 0 and freq[complementary_key] > 0:
                    diff = min(freq[key], freq[complementary_key])
                    res += 4*diff
                    freq[complementary_key] -= diff
                    freq[key] -= diff

        return res