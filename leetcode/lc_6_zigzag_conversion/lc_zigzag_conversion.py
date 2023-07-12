class Solution:
    def convert(self, s: str, numRows: int) -> str:

        column_distance = 2 * (numRows-1)
        res = ''

        if column_distance == 0:
            return s

        for row in range(numRows):
            for i in range(row, len(s), column_distance):
                res += s[i]
                if 0 < row < numRows-1 and i + column_distance - 2 * row < len(s):
                    res += s[i + column_distance - 2 * row]

        return res
