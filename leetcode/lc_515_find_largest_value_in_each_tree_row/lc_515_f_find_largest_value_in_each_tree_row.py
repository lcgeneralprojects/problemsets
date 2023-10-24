# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
from typing import Optional, List

from lc_common.lc_binary_tree import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        cur_row = [root]
        new_row = []

        while cur_row:
            row_maximum = -inf
            for node in cur_row:
                if node.val and node.val > row_maximum:
                    row_maximum = node.val

                if node.left is not None:
                    new_row.append(node.left)
                if node.right is not None:
                    new_row.append(node.right)

            res.append(row_maximum)

            cur_row = new_row
            new_row = []

        return res
