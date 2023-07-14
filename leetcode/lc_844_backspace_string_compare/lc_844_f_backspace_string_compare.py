class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stack_1 = []
        stack_2 = []

        for i in range(max(len(s), len(t))):
            if i < len(s):
                if s[i] == '#' and len(stack_1) > 0:
                    stack_1.pop()
                elif s[i] != '#':
                    stack_1.append(s[i])

            if i < len(t):
                if t[i] == '#' and len(stack_2) > 0:
                    stack_2.pop()
                elif t[i] != '#':
                    stack_2.append(t[i])

        return stack_1 == stack_2
    