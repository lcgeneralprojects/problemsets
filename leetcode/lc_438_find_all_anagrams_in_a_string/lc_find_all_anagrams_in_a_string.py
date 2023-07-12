from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cur = {}
        etalon = {}
        res = []

        for i in range(len(p)):
            if s[i] not in cur:
                cur[s[i]] = 1
            else:
                cur[s[i]] += 1

            if p[i] not in etalon:
                etalon[p[i]] = 1
            else:
                etalon[p[i]] += 1

        if cur == etalon:
            res.append(0)

        for i in range(1, len(s) - len(p) + 1):
            if s[i + len(p) - 1] not in cur:
                cur[s[i + len(p) - 1]] = 1
            else:
                cur[s[i + len(p) - 1]] += 1

            cur[s[i - 1]] -= 1

            if cur[s[i - 1]] == 0:
                del cur[s[i - 1]]

            if cur == etalon:
                res.append(i)

        return res

solution_obj = Solution()
s = "aaaaaaaaaa"
p = "aaaaaaaaaaaaa"

print(solution_obj.findAnagrams(s, p))