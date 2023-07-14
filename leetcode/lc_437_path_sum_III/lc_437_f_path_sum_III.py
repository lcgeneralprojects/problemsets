from collections import deque, defaultdict
from typing import Optional

from common.binary_tree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.res = 0
        self.possible_sums = defaultdict(int)
        self.possible_sums[targetSum] = 1

        def dfs(node: TreeNode, total):
            if node is None:
                return

            total += node.val
            self.res += self.possible_sums[total]
            self.possible_sums[total+targetSum] += 1        # If we later stumble upon a node
                                                            # for which total = old_total+target_sum,
                                                            # then we will have found a path for which the sum is
                                                            # total - old_total = target_sum
            dfs(node.left, total)
            dfs(node.right, total)
            self.possible_sums[total+targetSum] -=1
            return

        dfs(root, 0)

        return self.res

        """
        # Unfortunately, this only works for non-negative targetSum
        def dfs(root, vals):
            if root is None:
                return 0

            vals_copy = vals.copy()
            vals_copy.append(root.val)
            vals_sum = sum(vals_copy)

            while vals_copy and vals_sum > targetSum:
                vals_sum -= vals_copy[0]
                vals_copy.popleft()

            if vals_copy and vals_sum == targetSum:
                return 1 + dfs(root.left, vals_copy) + dfs(root.right, vals_copy)
            else:
                return dfs(root.left, vals_copy) + dfs(root.right, vals_copy)

        return dfs(root, deque())
        """