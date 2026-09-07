class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = defaultdict(int)
        length = 0
        l = 0
        for i, c in enumerate(s):
            while cache[c]:
                cache[s[l]] -= 1
                l += 1
            cache[c] += 1
            length = max(length, i - l + 1)
        
        return length