class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = {}
        res = 0
        flag = True  # This flag checks whether or not we have accounted for letters that occur an odd number of times in s

        for char in s:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

        for char in chars:
            if chars[char] % 2 == 0:
                res += chars[char]
            else:
                res += chars[char] - 1
                if flag:
                    res += 1
                    flag = False

        return res
    