from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n

        while left != right:
            mid = (left+right) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True

            if matrix[row][col] > target:
                right = mid
            else:
                left = mid+1

        if left >= m*n:
            return False

        return matrix[left // n][right % n] == target
