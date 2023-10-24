from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        left = 0
        right = len(nums)-1
        last_change = 0

        while left != right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle +1
                last_change = 1
            else: # If nums[middle] > target
                right = middle
                last_change = -1

        if nums[left] < target:
            return left+1
        else:
            return left
