from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # We are going to use two indices to iterate over nums1 and nums2
        # 'i' will be used for nums 1
        # 'j' will be used for nums 2

        # i = j = 0
        #
        # # Preventing out of bounds errors from occuring when dealing with i-1
        # if m > 0:
        #     while j < n and nums1[i] > nums2[j]:
        #         j += 1
        #     nums1 = [*nums2[:j], *nums1]
        #     i += 1
        # else:
        #     nums1 = [*nums2]
        #     return nums1    # Purely for testing
        #     # return        # Actual solution
        #
        # while i < m and j < n:
        #     if nums1[i] > nums2[j]:
        #         nums1 = [*nums1[:i], nums2[j], *nums1[i:]]
        #         j += 1
        #
        #     i += 1
        #
        # nums1 = [*nums1[:m+1], *nums2[j:n]]
        #
        # return nums1        # Purely for testing
        # ^DOES NOT PRODUCE THE NEEDED SIDE-EFFECTS

        i = m-1
        j = n-1
        k = m+n-1

        while j > -1:
            if i > -1 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        return nums1        # Purely for testing
