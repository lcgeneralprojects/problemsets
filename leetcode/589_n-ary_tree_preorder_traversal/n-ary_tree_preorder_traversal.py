"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]  # Stack for remembering the nodes we still need to visit.
        cur = root

        # Deep search
        while True:
            res.append(stack.pop().val)
            stack = stack + cur.children[::-1]

            if not stack:
                break

            cur = stack[-1]

        return res
