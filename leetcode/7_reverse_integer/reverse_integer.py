class Solution:
    def reverse(self, x: int) -> int:
        # Going for a detailed approach for practice purposes

        if x == 0:
            return 0

        res = 0

        leading_flag = True
        negative_flag = False
        if x < 0:
            negative_flag = True
            x = -x

        tmp = -2 ** 31
        if negative_flag:
            boundary = str(tmp)[1:]
        else:
            boundary = str(tmp + 1)[1:]

        # We want to check if there are digits greater than those in the boundary at any position in the case there
        # are as many digits in the result as there are in the boundary The following variable's value varies within
        # the set {-1, 0, 1} If, at any point, it becomes 1, then we are guaranteed to be dealing with overflow if
        # there are as many digits as in 2**31
        # If, at any point, it becomes -1
        potential_overflow = 0

        i = -1
        while True:
            i += 1
            tmp = x % 10

            if tmp == 0 and leading_flag:
                x = x // 10
                continue
            elif potential_overflow == 0:
                if tmp > int(boundary[i]):
                    potential_overflow = 1
                elif tmp < int(boundary[i]):
                    potential_overflow = -1

            res = res * 10 + tmp
            leading_flag = False

            x = x // 10

            if x == 0:
                break

        if i == len(boundary)-1 and potential_overflow == 1:
            return 0

        return res * ((-1) ** negative_flag)
