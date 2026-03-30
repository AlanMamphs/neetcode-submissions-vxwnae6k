from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for c in t:
            count_t[c] += 1
        
        l = 0
        res = ""
        for r in range(len(s)):
            count_s[s[r]] += 1

            while l <= r and all(count_s[char] >= count for char, count in count_t.items()):
                if not res or len(res) > r - l + 1:
                    res = s[l:r+1]
                count_s[s[l]] -= 1
                l += 1
            
        return res