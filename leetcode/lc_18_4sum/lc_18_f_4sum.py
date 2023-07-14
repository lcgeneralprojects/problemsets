from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left = j+1
                right = len(nums)-1
                new_target = target - nums[i] - nums[j]

                while left < right:
                    if nums[left] + nums[right] < new_target:
                        left += 1
                    elif nums[left] + nums[right] > new_target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right += 1

        return res