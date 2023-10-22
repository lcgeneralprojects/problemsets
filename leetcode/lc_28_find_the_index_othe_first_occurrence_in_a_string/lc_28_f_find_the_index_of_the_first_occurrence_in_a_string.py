class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Primitive solution
        # Another idea: keep a dictionary of positions of letters in the needle string,
        # find the letter that occurs the latest in the haystack,
        # check if it happens to be in a substring equal to the needle
        # if not, cut off the checked part of the haystack and repeat starting with step 2
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if i+j > len(haystack)-1 or haystack[i+j] != needle[j]:
                    break
                elif j == len(needle)-1:
                    res = i
                    return res

        return -1