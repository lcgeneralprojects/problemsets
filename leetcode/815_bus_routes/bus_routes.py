from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        # Edge case
        if source == target:
            return 0

        # Let's build our graph
        graph = defaultdict(set)

        for i in range(len(routes)):
            for stop in routes[i]:
                graph[stop].add(i)

        # Let's do BFS over our graph
        # We want to start at the source and the moment we arrive at the target, we are done
        # To do that, we want to check if the current route includes the stop; if it does not,
        # we proceed to add the unvisited routes which include the current stop to our queue of routes to check

        res = 0
        queue = deque()
        visited = set()

        # Initial construction of the queue
        for route in graph[source]:
            queue.append(route)
            visited.add(route)

        # BFS
        while queue:
            res += 1

            for i in range(len(queue)):
                cur = queue.popleft()
                # visited.add(cur)

                for stop in routes[cur]:
                    if stop == target:
                        return res

                    for route in graph[stop]:
                        if route not in visited:
                            queue.append(route)
                            visited.add(route)

        return -1
