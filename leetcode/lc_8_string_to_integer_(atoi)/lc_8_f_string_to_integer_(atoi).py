class Solution:
    def myAtoi(self, s: str) -> int:
        # Automata theoretical solution for training purposes

        res = 0

        cur_state = 0

        negative_flag = False
        # overflow_flag = False     # We don't need this in this solution
        boundary = (-2)**31
        digit_count = 0

        alphabet = [' ', '+', '-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # The automata graph is a dictionary that contains information about how a character should be processed in
        # any particular state of the automaton
        # The keys of this dictionary are states of the automaton
        # The values of this dictionary are dictionaries of the format {character: [state, function]}
        # The first item in the value in a sub-dictionary tells the automaton which state to go to
        # The second item in the value of a sub-dictionary tells us which function to call
        automata_graph = {state: {} for state in range(3)}

        def neg(*args):
            nonlocal  negative_flag
            negative_flag = True

        def modify(*args):
            nonlocal res
            nonlocal digit_count
            digit_count += 1
            res = res * 10 + int(args[0])

        def process(char):
            nonlocal cur_state
            if automata_graph[cur_state][char][1] is not None:
                automata_graph[cur_state][char][1](char)

            cur_state = automata_graph[cur_state][char][0]  # This order of function call and state change are
                                                            # important - otherwise we end up calling the function
                                                            # while in the wrong state

        for char in alphabet:
            if char == ' ':
                automata_graph[0][char] = [0, None]
            elif char == '+':
                automata_graph[0][char] = [1, None]
            elif char == '-':
                automata_graph[0][char] = [1, neg]
            elif char.isdigit():
                if char == '0':
                    automata_graph[0][char] = [1, None]
                else:
                    automata_graph[0][char] = [2, modify]
                automata_graph[1][char] = [2, modify]
                automata_graph[2][char] = [2, modify]

        for char in s:
            if char in automata_graph[cur_state].keys():
                process(char)
            else:
                break

        if negative_flag:
            res = -res
        else:
            boundary = (boundary+1)*(-1)

        """boundary_str = str(boundary)
        if digit_count > len(boundary_str):
            return (-1)**negative_flag * boundary
        elif digit_count == len(boundary_str):
            
            for char in res:
                if """

        if abs(res) > abs(boundary):
            res = boundary

        return res


# The following is a top solution on Leetcode
# Comments are mine (with one exception)
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()       # Removing the leading whitespaces
        if len(s) == 0:     # Edge case? Kind of. Otherwise we are going to try accessing an out-of-range value
            return 0

        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':   # We want to cut off the sign even if the sign value will be the same as in the next case
            sign = 1
            s = s[1:]
        else:
            sign = 1

        # digits = [str(i) for i in range(0, 10)]   # Not my comment
        result = 0
        for c in s:
            if not c.isdigit():
                break
            else:
                result = result * 10 + int(c)

        result = sign * result      # We assume that we can store result using more than 32 bits of memory
        UPPER_LIMIT = 2 ** 31 - 1
        LOWER_LIMIT = -2 ** 31
        if result < LOWER_LIMIT:
            return LOWER_LIMIT
        elif result > UPPER_LIMIT:
            return UPPER_LIMIT
        else:
            return result
            """