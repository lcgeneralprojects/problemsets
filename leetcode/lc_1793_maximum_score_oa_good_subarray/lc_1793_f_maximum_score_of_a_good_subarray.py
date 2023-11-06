from math import inf
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # def recursion(left, right, minimum):
        #     # if left < 0 or right > len(nums):
        #     #     return -inf
        #     while left-1 >= 0 and nums[left-1] >= minimum:
        #         left -= 1
        #     while right+1 < len(nums) and nums[right+1] >= minimum:
        #         right += 1
        #
        #     tmp_list = [(right-left+1)*minimum]
        #
        #     if left-1 >= 0:
        #         tmp_list.append(recursion(left-1, right, nums[left-1]))
        #     if right+1 < len(nums):
        #         tmp_list.append(recursion(left, right+1, nums[right+1]))
        #
        #     return max(tmp_list)
        #
        # return recursion(k, k, nums[k])
        # ^ TOO SLOW

        # # The search is happening too slow
        # def binary_search(left, right, target, nums):
        #     if right == -1:
        #         return 0
        #
        #     middle = (left+right) // 2
        #     middle_value = nums[middle]
        #     while left != right:
        #         if target > middle_value:
        #             left = middle + 1
        #         elif target < middle_value:
        #             right = middle
        #
        #         middle = (left + right) // 2
        #         middle_value = nums[middle]
        #
        #     if target <= middle_value:
        #         return middle
        #     elif target > middle_value:
        #         return middle+1
        #
        # def solve(nums, k):
        #     current_minimum = nums[k]
        #     res = nums[k]
        #     for right in range(k+1, len(nums)):
        #         if nums[right] < current_minimum:
        #             left = binary_search(0, k-1, current_minimum, nums)
        #             res = max(res, (right-left)*current_minimum) # (right-1)-left+1 = right-left
        #             current_minimum = nums[right]
        #
        #         if right == len(nums)-1:
        #             left = binary_search(0, k - 1, current_minimum, nums)
        #             res = max(res, (right - left + 1) * current_minimum)
        #
        #     return res
        #
        #
        # # The following piece of code is meant to set the values in the list to the minima that are to be encountered
        # # up to that point in the corresponding 'half' of the list when moving away from index k
        # current_minimum = nums[k]
        # for i in reversed(range(k)):
        #     if nums[i] < current_minimum:
        #         current_minimum = nums[i]
        #     else:
        #         nums[i] = current_minimum
        #
        # current_minimum = nums[k]
        # for i in range(k+1, len(nums)):
        #     if nums[i] < current_minimum:
        #         current_minimum = nums[i]
        #     else:
        #         nums[i] = current_minimum
        #
        # # Calling the solving function
        # return max(solve(nums, k), solve(list(reversed(nums)), len(nums)-k-1))
        # # ^ STILL TOO SLOW, even with the version for the solve function from the editorial

        left = right = k
        cur_min = res = nums[k]
        n = len(nums)

        while 0 < left or right < n-1:
            if (nums[left-1] if left > 0 else 0) > (nums[right+1] if right < n-1 else 0):
                left -= 1
                cur_min = min(cur_min, nums[left])
            else:
                right += 1
                cur_min = min(cur_min, nums[right])

            res = max(res, cur_min * (right-left+1))

        return res
