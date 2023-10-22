class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        paren_stack = [-1]

        for i in range(len(s)):
            if s[i] == '(':
                paren_stack.append(i)
            elif len(paren_stack) == 1:
                paren_stack[0] = i
            else:
                paren_stack.pop()
                res = max(res, i - paren_stack[-1])

        return res