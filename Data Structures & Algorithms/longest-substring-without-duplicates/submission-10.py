class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        res = 0
        l = 0
        for r, c in enumerate(s):
            counts[c] += 1

            while counts[c] > 1:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r + 1 - l)
        return res