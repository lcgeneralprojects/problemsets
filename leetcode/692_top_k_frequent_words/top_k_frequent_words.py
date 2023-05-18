from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = [k for k, v in sorted(Counter(sorted(words)).items(), key=lambda item: item[1], reverse=True)]

        return res[:k]
    