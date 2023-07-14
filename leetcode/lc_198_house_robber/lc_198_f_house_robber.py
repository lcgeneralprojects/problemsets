from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        """

        mem = [0, 0, 0]

        for i in range(len(nums)):
            mem[2] = max(nums[i] + mem[1], mem[0])
            mem[1] = mem[0]
            mem[0] = mem[2]

        return mem[0]