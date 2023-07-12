from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer = list(range(len(grid[0])))

        for i in range(len(grid)):
            for j in range(len(answer)):
                if answer[j] == -1:
                    continue

                pre_calc = answer[j] + grid[i][answer[j]]

                if pre_calc not in range(len(grid[0])) or grid[i][answer[j]] + grid[i][pre_calc] == 0:
                    answer[j] = -1
                else:
                    answer[j] = pre_calc

        return answer
