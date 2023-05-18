from collections import defaultdict
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs solution; we start at the coastline, and then go deeper into the island,
        # filling an auxiliary dictionary with values for flags corresponding to the conditions that interest us

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        stack = []
        auxiliary_dictionary = defaultdict(lambda: [False, False])  # [Pacific, Atlantic]

        m = len(heights)
        n = len(heights[0])

        for i in range(m):
            stack.append((i, 0))
            auxiliary_dictionary[(i, 0)][0] = True
            stack.append((i, n - 1))
            auxiliary_dictionary[(i, n - 1)][1] = True

        for j in range(1, n - 1):
            stack.append((0, j))
            auxiliary_dictionary[(0, j)][0] = True
            stack.append((m - 1, j))
            auxiliary_dictionary[(m - 1, j)][1] = True

        # Allowing myself some inefficiencies here
        auxiliary_dictionary[(0, n - 1)][0] = True
        auxiliary_dictionary[(0, n - 1)][1] = True
        auxiliary_dictionary[(m - 1, 0)][0] = True
        auxiliary_dictionary[(m - 1, 0)][1] = True

        # Initial stack is formed by now

        res = []

        while stack:
            for i in range(len(stack)):
                cur_cell = stack.pop()
                pacific_flag = auxiliary_dictionary[cur_cell][0]
                atlantic_flag = auxiliary_dictionary[cur_cell][1]

                for direction in directions:
                    next_cell = tuple(map(sum, zip(cur_cell, direction)))

                    if next_cell[0] not in range(m) or next_cell[1] not in range(n) \
                            or auxiliary_dictionary[next_cell] == auxiliary_dictionary[cur_cell] \
                            or heights[next_cell[0]][next_cell[1]] < heights[cur_cell[0]][cur_cell[1]]:
                            # We are moving in from the coastline,
                            # so we are checking if the water could have flown from the next cell to the current one
                        continue
                    auxiliary_dictionary[next_cell] = [
                        auxiliary_dictionary[next_cell][0] or auxiliary_dictionary[cur_cell][0],
                        auxiliary_dictionary[next_cell][1] or auxiliary_dictionary[cur_cell][1]]
                    stack.append(next_cell)

        res = []

        # Allowing myself some inefficiencies here
        for row in range(m):
            for column in range(n):
                if auxiliary_dictionary[(row, column)] == [True, True]:
                    res.append([row, column])

        return res
