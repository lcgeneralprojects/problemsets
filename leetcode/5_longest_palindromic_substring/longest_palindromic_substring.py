class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''

        # Naive solution, O(n^2)
        for i in range(len(s)):
            for j in range(i, len(s)):
                # Let's not call functions all the time
                if s[i] == s[j] and j - i + 1 > len(res):
                    if s[i:j + 1] == ''.join(reversed(s[i:j + 1])):
                        res = s[i:j + 1]

        return res