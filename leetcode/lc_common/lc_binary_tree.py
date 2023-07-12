from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dequeToTree(input_list: deque):
    if not input_list:
        return None

    head = TreeNode(input_list.popleft())
    cur_level = [head]

    while input_list:
        next_level = []

        for node in cur_level:

            # Adding the left child
            if not input_list:
                break

            tmp = input_list.popleft()

            if tmp == 'null':
                node.left = None
            else:
                node.left = TreeNode(val=tmp)
                next_level.append(node.left)

            # Adding the right child
            if not input_list:
                break

            tmp = input_list.popleft()

            if tmp == 'null':
                node.right = None
            else:
                node.right = TreeNode(val=tmp)
                next_level.append(node.right)

        cur_level = next_level

    return head



def treeToDeque(input_root: TreeNode):
    return None