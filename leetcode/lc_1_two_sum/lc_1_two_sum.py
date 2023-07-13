class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        previous_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in previous_map:
                return (previous_map[diff], i)
            previous_map[n] = i