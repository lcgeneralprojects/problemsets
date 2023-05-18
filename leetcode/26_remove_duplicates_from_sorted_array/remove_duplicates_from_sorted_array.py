class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = len(nums)
        while True:
            if i + 1 == len(nums):
                break

            if nums[i] == nums[i + 1]:
                del nums[i + 1]
                k = k - 1
            else:
                i += 1

        return k