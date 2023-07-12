from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()
        res = []

        i = j = counter = 0

        while i in range(len(matrix)) and j in range(len(matrix[0])) and (i, j) not in visited:
            visited.add((i, j))
            res.append(matrix[i][j])

            pre_i, pre_j = map(lambda x, y: x + y, (i, j), directions[counter % 4])

            if pre_i not in range(len(matrix)) or pre_j not in range(len(matrix[0])) or (pre_i, pre_j) in visited:
                counter += 1
                i, j = map(lambda x, y: x + y, (i, j), directions[counter % 4])
            else:
                i, j = pre_i, pre_j

        return res

solution_obj = Solution()

matrix = [[1]]

print (solution_obj.spiralOrder(matrix))