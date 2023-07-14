import heapq
from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        freqs_dict = Counter(tasks)
        freqs_heap = [-freq for freq in freqs_dict.values()]
        heapq.heapify(freqs_heap)
        cooldowns = deque()
        res = 0

        while freqs_heap or cooldowns:
            res += 1

            if freqs_heap:
                #cooldowns.append([1+heapq.heappop(freqs_heap), res+n])
                precalc = 1+heapq.heappop(freqs_heap)
                if precalc < 0:
                    cooldowns.append([precalc, res+n])

            if cooldowns and cooldowns[0][1] == res:
                heapq.heappush(freqs_heap, cooldowns.popleft()[0])

        return res

        """
        freqs = Counter(tasks)
        cooldowns = defaultdict(int)  # Setting starting active cooldowns to 0
        schedule = []

        while sum(freqs.values()) != 0:
            available_tasks_flag = 0
            freqs_sorted = {k: v for k, v in sorted(freqs.items(), key=lambda item: item[1], reverse=True)}

            for task in freqs_sorted:
                available_tasks_flag = 0

                if cooldowns[task] < 1 and freqs[task] > 0:
                    schedule.append(task)

                    for key in cooldowns:
                        cooldowns[key] -= 1

                    cooldowns[task] = n
                    freqs[task] -= 1

                    available_tasks_flag = 1

                    break

            if available_tasks_flag == 0:
                schedule.append('')

                for key in cooldowns:
                    cooldowns[key] -= 1
        

        return len(schedule)
        """
