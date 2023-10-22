import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        """
        def dfs(cell: List[int]):
            if not 0 <= cell[0] < len(grid) or not 0 <= cell[1] < len(grid[0]) or cell in visited or grid[cell[0]][cell[1]] == '0':
                return

            visited.append(cell)
            for direction in dir:
                dfs([sum(x) for x in zip(cell, direction)])
            return
        """

        def bfs(x, y):
            to_visit = collections.deque()
            to_visit.append((x, y))

            while to_visit:
                cell = to_visit.popleft()
                visited.add(cell)

                for direction in dir:
                    cur = (cell[0]+direction[0], cell[1]+direction[1])
                    if cur[0] in range(len(grid)) and cur[1] in range(len(grid[0])) and cur not in visited and grid[cur[0]][cur[1]] == "1":
                        to_visit.append(cur)

            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    res += 1
                    # dfs([i, j])
                    bfs(i, j)

        return res


solution_object = Solution()
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

print(solution_object.numIslands(grid))




"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = '0'

            # top
            if 0 <= r - 1 and grid[r - 1][c] == '1': dfs(r - 1, c)
            # bottom
            if r + 1 < rows and grid[r + 1][c] == '1': dfs(r + 1, c)
            # left
            if 0 <= c - 1 and grid[r][c - 1] == '1': dfs(r, c - 1)
            # right
            if c + 1 < cols and grid[r][c + 1] == '1': dfs(r, c + 1)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands
"""