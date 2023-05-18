# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSubtree(self, root, boundaries):
        if root is None:
            return True
        elif not boundaries[0] < root.val < boundaries[1]:
            return False

        return self.checkSubtree(root.left, [boundaries[0], min(boundaries[1], root.val)]) and self.checkSubtree(
            root.right, [max(boundaries[0], root.val), boundaries[1]])

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkSubtree(root, [float('-inf'), float('inf')])
