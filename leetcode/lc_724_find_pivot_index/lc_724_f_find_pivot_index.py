class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_part = [0]
        right_part = [0]

        for i in range(1, len(nums)):
            left_part.append(left_part[i - 1] + nums[i - 1])
            right_part.append(right_part[i - 1] + nums[-i])

        for i in range(len(nums)):
            if left_part[i] == right_part[-1 - i]:
                return i

        return -1