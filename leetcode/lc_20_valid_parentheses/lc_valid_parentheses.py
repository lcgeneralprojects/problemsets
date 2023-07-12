class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        res = True

        for i in range(len(s)):
            try:
                if s[i] in ['(', '[', '{']:
                    stack.append(s[i])
                elif valid_pairs[stack.pop()] != s[i]:
                    res = False
                    break
            except:
                res = False

        if stack != []:
            res = False

        return res