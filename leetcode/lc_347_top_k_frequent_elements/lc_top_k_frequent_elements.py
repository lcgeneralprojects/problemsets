from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        freqs = [[] for letter in range(max(count.values())+1)]

        for letter, freq in count.items():
            freqs[freq].append(letter)

        res = []

        # Iterating over freqs in reverse order
        # Not using for i in range(k), as the same frequency can correspond to multiple letters
        for freq in range(len(freqs) - 1, 0, -1):
            for letter in freqs[freq]:
                res.append(letter)
                if len(res) == k:
                    return res
