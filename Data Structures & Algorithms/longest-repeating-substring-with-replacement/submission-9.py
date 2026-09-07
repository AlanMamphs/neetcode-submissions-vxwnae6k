class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        res = 0
        for i, c in enumerate(s):
            counts[c] += 1
            while (i - l) + 1 > max(counts.values()) + k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        
        return res


