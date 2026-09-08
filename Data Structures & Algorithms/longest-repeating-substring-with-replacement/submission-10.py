class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        counts = defaultdict(int)
        l = 0
        for r, c in enumerate(s):
            counts[c] += 1
            while sum(counts.values()) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res