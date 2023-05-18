from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def rec(List, Num):
            s = sum(List)
            if s == target:
                res.append(List)
            elif s < target:
                for i in range(Num, len(candidates)):
                    rec(List + [candidates[i]], i)

        rec([], 0)
        return res
    