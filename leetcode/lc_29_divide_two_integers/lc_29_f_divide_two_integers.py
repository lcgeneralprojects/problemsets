class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        sign = 1
        INT_MAX = 2147483647    # 2^31-1
        INT_MIN = 2147483648    # 2^31

        if (dividend > 0 > divisor) or (dividend < 0 < divisor):
            sign = -1

        # Consider that these are unacceptable side effects in real programs
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Primitive solution is too slow
        # quotient = 0
        # while dividend >= divisor:
        #     quotient += 1
        #     dividend -= divisor

        quotient = 0
        while dividend >= divisor:
            tmp = divisor << 1
            power = 1
            # If the quotient is 2, this loop will run twice with the intermediate quotients being 1 both times
            # - not elegant
            while dividend - tmp >= divisor:
                tmp = tmp << 1
                power += 1
            intermediate_quotient = 1 << power-1
            dividend -= tmp >> 1
            if sign == 1:
                if INT_MAX - intermediate_quotient > quotient:
                    quotient += intermediate_quotient
                else:
                    return INT_MAX
            elif sign == -1:
                if INT_MIN - intermediate_quotient > quotient:
                    quotient += intermediate_quotient
                else:
                    return -INT_MIN

        if sign == -1:
            quotient = 0-quotient

        return quotient