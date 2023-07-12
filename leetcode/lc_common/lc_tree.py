class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = []


class Tree:
    def __init__(self, val=None):
        self.root = TreeNode(val)