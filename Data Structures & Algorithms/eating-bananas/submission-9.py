class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)

        l = 1
        r = max_speed
        res = r
        while l <= r:
            m = l + (r - l) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            if hours > h:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1
        return res


