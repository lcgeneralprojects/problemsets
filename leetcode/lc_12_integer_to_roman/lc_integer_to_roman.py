class Solution:
    def intToRoman(self, num: int) -> str:

        # The following is a constant list that contains lists that correspond to rules for translation of integers
        # in base 10 to their forms in Roman numerals
        # Each of the 'rules' is a list of three elements
        # The first element is an integer
        # The second element is a corresponding Roman numeral
        # The third element is an index of
        # the rule that corresponds to the lesser Roman numeral that can precede this one
        DEC_TO_ROMAN = [[1000, 'M', 2], [500, 'D', 2], [100, 'C', 4],
                        [50, 'L', 4], [10, 'X', 6], [5, 'V', 6], [1, 'I', None]]

        res = ''

        for rule in DEC_TO_ROMAN:
            div = num // rule[0]
            subtraction_flag = (rule[2] is not None and (rule[0] * (div+1) - num) <= DEC_TO_ROMAN[rule[2]][0])

            res += rule[1] * div
            num -= div * rule[0]

            if subtraction_flag:
                res += (DEC_TO_ROMAN[rule[2]][1] + rule[1]) * subtraction_flag
                num -= rule[0] - DEC_TO_ROMAN[rule[2]][0]

        return res
