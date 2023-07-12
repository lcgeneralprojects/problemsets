class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res = ""

        i = 0
        flag = False
        while True:
            for word in strs:
                if (i > len(word) - 1) or (word[i] != strs[0][i]):
                    flag = True
                    break

            if flag == True:
                break
            else:
                res += strs[0][i]
                i += 1

        return res
