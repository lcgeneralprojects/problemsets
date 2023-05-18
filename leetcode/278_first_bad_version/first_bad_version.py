# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        cur = (left + right) // 2

        while left != right:
            if isBadVersion(cur):
                right = cur
            else:
                left = cur + 1

            cur = (left + right) // 2

        return cur
