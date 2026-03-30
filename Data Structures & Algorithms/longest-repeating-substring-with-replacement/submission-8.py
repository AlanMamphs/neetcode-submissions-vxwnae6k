from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_s = defaultdict(int)
        res  = 0
        l = 0
        for r in range(len(s)):
            count_s[s[r]] += 1
            while max(count_s.values()) + k < r - l + 1: # O(constant)
                count_s[s[l]] -= 1
                l += 1
            else:
                res = max(r - l + 1, res)
        
        return res
