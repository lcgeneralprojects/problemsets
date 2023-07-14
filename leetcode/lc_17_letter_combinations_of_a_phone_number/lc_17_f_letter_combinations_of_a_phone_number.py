from typing import List
from common.tree import TreeNode, Tree


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        character_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                          '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        res_tree = Tree('')
        cur_level = [res_tree.root]

        for i in range(len(digits)):
            next_level = []
            for node in cur_level:
                for character in character_dict[digits[i]]:
                    new_node = TreeNode(node.val + character)
                    node.children.append(new_node)
                    next_level.append(new_node)
            cur_level = next_level

        res = []
        for node in cur_level:
            if node.val != '':
                res.append(node.val)

        return res
