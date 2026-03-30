from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = float('inf')
        while l <= r:
            m = l + (r - l) // 2
            x = sum(ceil(p / m) for p in piles)
            if x <= h:
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1
        return res