from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def transform(index, k, length):
            return (index - k) % length

        # This dfs is used to find the pivot of rotation of the input array/list
        def dfs(l, r, arr):
            if l < r:
                if arr[l] < arr[r]:         # Correctly-ordered segment of the array
                    return 0
                else:                       # Problematic segment of the array
                    mid = (l + r) // 2
                    if arr[mid] > arr[mid+1]:
                        return len(arr) - (mid+1)
                    else:
                        return dfs(l, mid, arr) + dfs(mid + 1, r, arr)

            else:
                return 0

        if len(nums) == 1:
            if target in nums:
                return 0
            else:
                return -1

        nums_length = len(nums)
        left = 0
        right = nums_length-1

        # Let's find the pivot of nums
        k = dfs(left, right, nums)

        # Let's find the target number
        while left != right:
            mid = (left + right) // 2
            mid_transformed = transform(mid, k, nums_length)

            if nums[mid_transformed] == target:
                return mid_transformed

            if nums[mid_transformed] > target:
                right = mid
            else:
                left = mid+1

        if left not in range(nums_length) or nums[transform(left, k, nums_length)] != target:
            return -1
        else:
            return transform(left, k, nums_length)
