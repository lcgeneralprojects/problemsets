from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        mem = defaultdict(int)
        bulls = 0
        cows = 0

        for digit in secret:
            mem[digit] = secret.count(digit)

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                mem[guess[i]] -= 1


        for i in range(len(secret)):
            if mem[guess[i]] > 0:
                cows += 1
                mem[guess[i]] -= 1

        return f"{bulls}A{cows}B"

solution_obj = Solution()
secret = "1122"
guess = "1222"

print(solution_obj.getHint(secret, guess))