# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from common.binary_tree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            if node is None or self.counter > self.target:
                return

            dfs(node.left)

            self.counter += 1
            if self.counter == self.target:
                self.res = node.val

            dfs(node.right)

            return

        self.counter = 0
        self.target = k
        self.res = -1

        dfs(root)

        return self.res
