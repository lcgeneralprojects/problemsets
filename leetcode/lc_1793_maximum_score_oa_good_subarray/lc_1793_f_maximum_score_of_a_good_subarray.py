from math import inf
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def recursion(left, right, minimum):
            # if left < 0 or right > len(nums):
            #     return -inf
            while left-1 >= 0 and nums[left-1] >= minimum:
                left -= 1
            while right+1 < len(nums) and nums[right+1] >= minimum:
                right += 1

            tmp_list = [(right-left+1)*minimum]

            if left-1 >= 0:
                tmp_list.append(recursion(left-1, right, nums[left-1]))
            if right+1 < len(nums):
                tmp_list.append(recursion(left, right+1, nums[right+1]))

            return max(tmp_list)

        return recursion(k, k, nums[k])
