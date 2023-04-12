class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
# The following assignments serve two purposes: firstly, this deals with the out-of-range errors when nums2 is empty
        # secondly, performing binary searches on the shorter list is more efficient
        if len(nums1) <= len(nums2):
            nums1_local = nums1
            nums2_local = nums2
        else:
            nums1_local = nums2
            nums2_local = nums1

        TOTAL_LEN = len(nums1_local) + len(nums2_local)
        boundaries = [0, len(nums1_local)-1]    # This variable represents the boundaries within which the correct
                                                # partition of nums1 is contained No such variable is needed for
                                                # nums2, as all the relevant values can be derived
                                                # from the corresponding values for nums1

        while True:
            # Within the loop, we are looking for partitions of nums1 and nums2, defined by the variables cur1 and
            # cur2 as their greatest elements, such that elements in each of those partitions are no greater than the
            # elements outside of the partitions in both of the lists (given that both lists are already sorted,
            # we just need to compare values from each of the partitions to the values from the opposing list)

            # The following two variables represent the pointers to the greater boundaries of the current partitions
            # of nums1 and nums2
            cur1 = sum(boundaries)//2
            cur2 = TOTAL_LEN//2 - cur1 - 2

            # Accounting for out-of-range errors by storing numbers on the edges of the partitions in special variables
            nums1_lower = nums1_local[cur1] if cur1 >= 0 else float('-inf')
            nums1_greater = nums1_local[cur1+1] if cur1+1 < len(nums1_local) else float('inf')
            nums2_lower = nums2_local[cur2] if cur2 >= 0 else float('-inf')
            nums2_greater = nums2_local[cur2+1] if cur2+1 < len(nums2_local) else float('inf')

            # Checking for the correctness of the choice of partitions
            if nums1_lower <= nums2_greater and nums2_lower <= nums1_greater:
                if TOTAL_LEN % 2 == 0:
                    return (max(nums1_lower, nums2_lower) + min(nums1_greater, nums2_greater))/2
                else:
                    return min(nums1_greater, nums2_greater)
            elif nums1_lower > nums2_greater:
                boundaries[1] = cur1-1
            else:
                boundaries[0] = cur1+1