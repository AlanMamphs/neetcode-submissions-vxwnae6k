import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        max_n = max(piles)
        r = max_n
        res = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            count_h = 0

            for p in piles:
                count_h += math.ceil(p /(mid))
            if count_h <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
            

