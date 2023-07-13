class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        num = n

        while num not in visited:
            visited.add(num)
            tmp = 0

            while num > 0:
                tmp += (num % 10) ** 2
                num = num // 10

            num = tmp

            if num == 1:
                return True

        return False
