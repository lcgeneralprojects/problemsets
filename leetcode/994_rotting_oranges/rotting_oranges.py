from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten = []  # Stack of rotten oranges

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    rotten.append((row, column))

        time = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        new_rotten = []
        progress_flag = 0  # Check if any new oranges went bad

        while rotten != []:
            cur = rotten.pop()

            for direction in directions:
                row, column = tuple(map(sum, zip(cur, direction)))

                if row in range(len(grid)) and column in range(len(grid[0])) and grid[row][column] == 1:
                    new_rotten.append((row, column))
                    grid[row][column] = 2
                    progress_flag = 1

            if rotten == [] and progress_flag == 1:
                rotten = new_rotten
                new_rotten = []
                progress_flag = 0
                time += 1


        for row in grid:
            if 1 in row:
                return -1

        return time