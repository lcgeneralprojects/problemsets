from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Consider the original string as a graph, with adjacent vertices corresponding to adjacent letters
        # adjacentPairs list contains information about all pairs of adjacent vertices in our graph
        # What we want is to construct a Hamiltonian path, which has to start with a vertex of degree 1 in our case
        # THIS SOLUTION IS TOO SLOW
        adjacency_dict = defaultdict(list)
        for pair in adjacentPairs:
            adjacency_dict[pair[0]].append(pair[1])
            adjacency_dict[pair[1]].append(pair[0])

        potential_starts = [key for key in adjacency_dict.keys() if len(adjacency_dict[key]) == 1]

        # At this point, potential_starts should contain exactly two elements. We can pick either as a start
        cur_node = potential_starts[0]
        res = [cur_node]
        next_node = adjacency_dict[cur_node][0]
        while True:
            # next_node = adjacency_dict[cur_node][0]
            # # adjacency_dict[next_node].remove(cur_node)
            # if len(adjacency_dict[next_node]) == 2 and adjacency_dict[next_node][0] == cur_node:
            #     adjacency_dict[next_node][0] = adjacency_dict[next_node][1]
            # res.append(next_node)
            # cur_node = next_node
            # if len(adjacency_dict[cur_node]) == 1:
            #     break
            tmp = next_node
            res.append(tmp)
            if tmp in potential_starts:
                break
            else:
                for node in adjacency_dict[tmp]:
                    if node != cur_node:
                        next_node = node
            cur_node = tmp

        return res
