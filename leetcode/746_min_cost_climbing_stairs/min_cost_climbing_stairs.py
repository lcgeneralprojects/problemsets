from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = [0, cost[-1]]

        for i in range(len(cost) - 2, -1, -1):
            mem.append(cost[i] + min(mem[-1], mem[-2]))

        return min(mem[-1], mem[-2])
