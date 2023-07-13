# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from common.binary_tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return (-1, -1)

            left, right = dfs(root.left), dfs(root.right)
            cur_max = max(left[1], right[1], 2 + left[0] + right[0])

            return (1 + max(left[0], right[0]), cur_max)

        return dfs(root)[1]
    