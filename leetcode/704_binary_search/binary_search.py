from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        boundaries = [0, len(nums)]
        while boundaries[0] != boundaries[1]:
            middle = int(sum(boundaries) / 2)
            if target < nums[middle]:
                boundaries[1] = middle
            else:
                if boundaries[0] == middle:
                    break
                boundaries[0] = middle

        if nums[boundaries[0]] != target:
            return -1
        else:
            return boundaries[0]
