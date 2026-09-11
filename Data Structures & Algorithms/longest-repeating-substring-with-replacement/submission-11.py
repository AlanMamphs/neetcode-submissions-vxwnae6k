class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)

        l = 0
        res = 0
        for r, c in enumerate(s):
            counts[c] += 1

            while r - l + 1 - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r + 1 - l)
        return res