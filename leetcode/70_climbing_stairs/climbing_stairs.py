class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return 1

        mem_1 = mem_2 = 1

        for i in range(2, n):
            tmp = mem_2
            mem_2 += mem_1
            mem_1 = tmp

        return mem_2

solution_object = Solution()

print(solution_object.climbStairs(2))