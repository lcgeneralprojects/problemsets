# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        cur_level = [root]
        next_level = []

        while True:
            if not cur_level:
                break

            sub_res = []

            for node in cur_level:
                sub_res.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            cur_level = next_level
            next_level = []
            res.append(sub_res)

        return res