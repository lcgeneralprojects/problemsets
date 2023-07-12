class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_chars = {}
        substr_start = 0
        longest_substr_length = 0
        cur_substr_length = 0
        cur_index = 0

        while cur_index < len(s):
            if s[cur_index] not in substr_chars:
                substr_chars[s[cur_index]] = cur_index
                cur_index += 1

                if cur_index - substr_start > longest_substr_length:
                    longest_substr_length = cur_index - substr_start

            else:
                del substr_chars[s[substr_start]]
                substr_start += 1

        return longest_substr_length
