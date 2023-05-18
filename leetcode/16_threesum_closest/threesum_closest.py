class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n = len(nums)
        nums.sort()
        min_diff = math.inf
        res = 0

        for a in range(n):
            b = a + 1
            c = n - 1

            while (b < c):
                cur_sum = nums[a] + nums[b] + nums[c]
                cur_diff = abs(cur_sum - target)
                if (cur_diff < min_diff):
                    min_diff = cur_diff
                    res = cur_sum
                if (cur_sum == target):
                    return target
                elif (cur_sum < target):
                    b += 1
                else:
                    c -= 1

        return res