class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left_m = prices[0]

        for p in prices:
            res = max(res, p - left_m)
            left_m = min(p, left_m)
        return res