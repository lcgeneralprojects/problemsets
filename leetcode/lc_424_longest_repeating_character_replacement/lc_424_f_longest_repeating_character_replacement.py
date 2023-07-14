class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        mem = {}
        res = 0

        for right in range(len(s)):
            mem[s[right]] = mem.get(s[right], 0) + 1

            while right - left + 1 - max(mem.values()) > k:
                mem[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
