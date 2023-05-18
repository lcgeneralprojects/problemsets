import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones[:]
        heapq.heapify(heap)

        while len(heap) > 1:
            heaviest = [heapq.heappop([heap[-1]]), -heapq.heappop([heap[-1]])]
            heapq.heappush(heap, abs(sum(heaviest)))

        return sum(heap)

solution_obj = Solution()

stones = [2,7,4,1,8,1]

print(solution_obj.lastStoneWeight(stones))