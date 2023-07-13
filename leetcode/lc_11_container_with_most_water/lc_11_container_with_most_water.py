from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Move from both ends towards the center and consider minimum heights on the left and on the right. Consider
        # why lower walls will not improve our result

        left, right = 0, len(height) - 1

        max_area = 0

        while left != right:
            cur_area = (right - left) * min(height[left], height[right])
            if cur_area > max_area:
                max_area = cur_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
