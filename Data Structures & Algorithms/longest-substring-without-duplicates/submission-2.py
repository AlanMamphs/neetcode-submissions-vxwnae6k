class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        unique = {}
        l = 0
        for r in range(len(s)):
            if s[r] not in unique:
                longest = max(longest, len(unique) + 1)
            else:
                for c in s[l:unique[s[r]]]:
                    del unique[c]
                l = unique[s[r]] + 1
            unique[s[r]] = r

        return longest
            