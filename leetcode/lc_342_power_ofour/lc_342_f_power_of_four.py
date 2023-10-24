import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and (n & (n-1)) and (n & 0b1010101010101010101010101010101) != 0
        return n > 0 and math.log(n, 4).is_integer()
