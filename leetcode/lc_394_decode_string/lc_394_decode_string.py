class Solution:
    def decodeString(self, s: str) -> str:
        res = []

        for i in range(len(s)):
            if s[i] != ']':
                res.append(s[i])
            else:
                substr = ''
                while res[-1] != '[':
                    substr = res.pop() + substr
                res.pop()

                counter = ''
                while res and res[-1].isdigit():
                    counter = res.pop() + counter
                res.append(int(counter) * substr)

        return ''.join(res)

solution_obj = Solution()

s = "100[leetcode]"

print(solution_obj.decodeString(s))