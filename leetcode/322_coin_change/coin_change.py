import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [math.inf] * (amount + 1)
        arr[0] = 0

        for cur_amount in range(1, amount + 1):
            for coin in coins:
                if cur_amount - coin >= 0:
                    # The following code's meaning: if we can get to a previously-visited amount of coins,
                    # we can get from there to cur_amount in one go
                    arr[cur_amount] = min(arr[cur_amount], 1 + arr[cur_amount - coin])

        return arr[amount] if arr[amount] < amount + 1 else -1
