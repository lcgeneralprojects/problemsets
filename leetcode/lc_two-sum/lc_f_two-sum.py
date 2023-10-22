class Solution(object):
    def twoSum(self, nums, target):
        previous_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in previous_map:
                return (previous_map[diff], i)
            previous_map[n] = i