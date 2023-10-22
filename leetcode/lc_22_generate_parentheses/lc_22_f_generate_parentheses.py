from typing import List


class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        # Depth-first search
        # The argument 'opening' refers to the number of opening parentheses in the current string s
        # The argument 'closing' refers to the number of closing parentheses in the current string s
        def dfs(opening, closing, s):
            if closing == n:
                res.append(s)

            if opening < n:
                dfs(opening+1, closing, s+'(')

            if closing < opening:
                dfs(opening, closing+1, s+')')


        res = []
        dfs(0, 0, '')
        return res