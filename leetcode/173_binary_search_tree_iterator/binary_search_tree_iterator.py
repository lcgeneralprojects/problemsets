# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from common.binary_tree import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.sub_trees = []
        cur = root

        while cur is not None:
            self.sub_trees.append(cur)
            cur = cur.left

    def next(self) -> int:

        res = self.sub_trees.pop()

        cur = res.right
        while cur is not None:
            self.sub_trees.append(cur)
            cur = cur.left

        return res.val

    def hasNext(self) -> bool:
        return self.sub_trees != []
