class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = dict()
        l = 0
        longest = 0
        for r in range(len(s)):
            if s[r] in store:
                l = max(store[s[r]] + 1, l)
            longest = max(r - l + 1, longest)
            
            store[s[r]] = r
        return longest
