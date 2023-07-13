from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_min = float(inf)

        for i in range(len(prices)):
            if prices[i] < cur_min:
                cur_min = prices[i]
            elif prices[i] - cur_min > max_profit:
                max_profit = prices[i] - cur_min

        return max_profit