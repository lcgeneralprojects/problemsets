class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []

        for i in range(m):
            grid.append([])
            for j in range(n):
                grid[i].append(1)

                if i > 0 and j > 0:
                    grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - 1

        return grid[m - 1][n - 1]
    