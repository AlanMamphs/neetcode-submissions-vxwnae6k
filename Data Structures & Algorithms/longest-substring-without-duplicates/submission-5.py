class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_char_index = dict()
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] in last_char_index:
                l = max(last_char_index[s[r]] + 1, l)
            longest = max(longest, r - l + 1)
            last_char_index[s[r]] = r
        return longest
