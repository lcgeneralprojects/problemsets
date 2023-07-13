class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Let's get rid of redundant patterns
        def trim(pattern):

            if len(pattern) < 4:
                return pattern

            i = 3
            while True:
                if i >= len(pattern):
                    break
                elif pattern[i] == '*' and pattern[i-1:i+1] == pattern[i-3:i-1]:
                    pattern = pattern[:i-1] + pattern[i+1:]
                else:
                    i += 1

            return pattern



        # Primary recursive function
        def recursion(string, pattern):

            string_length = len(string)
            pattern_length = len(pattern)

            # Let's separate the cases for the following '*' character and for everything else right at the root
            if pattern_length > 1 and pattern[1] == '*':
                # if string_length == 0:
                #     if pattern_length == 2:
                #         return True
                #     else:
                #         return False
                # elif string[0] != pattern[0] and pattern[0] != '.':
                if string_length == 0 or (string[0] != pattern[0] and pattern[0] != '.'):
                    return recursion(string, pattern[2:])
                else:
                    return recursion(string[1:], pattern) or recursion(string[1:], pattern[2:]) or recursion(string, pattern[2:])

            else:
                if string_length == 0 or pattern_length == 0:
                    if string_length == 0 and pattern_length == 0:
                        return True
                    else:
                        return False

                if string[0] != pattern[0] and pattern[0] != '.':
                    return False
                else:
                    return recursion(string[1:], pattern[1:])

        p = trim(p)
        return recursion(s, p)
