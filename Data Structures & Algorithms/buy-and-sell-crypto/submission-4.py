class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left_min = float('inf')
        for p in prices:
            left_min = min(left_min, p)
            res = max(p - left_min, res)
        return res