class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        let_to_num_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
                           'I': 1}  # a dictionary of letter-to-number correspondence
        cur_let = ''  # current highest-valued letter

        for letter in let_to_num_dict:
            if letter in s:
                cur_let = letter
                break

        for i in range(len(s)):
            if cur_let not in s[i:]:
                for letter in let_to_num_dict:
                    if letter in s[i:]:
                        cur_let = letter
                        break
            if s[i] == cur_let:
                res += let_to_num_dict[s[i]]
            else:
                res = res - let_to_num_dict[s[i]]

        return res