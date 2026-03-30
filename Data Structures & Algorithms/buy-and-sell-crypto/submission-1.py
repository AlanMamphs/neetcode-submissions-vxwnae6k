class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = prices[0]
        profit = 0
        for x in prices:
            left_min = min(left_min, x)
            profit = max(x - left_min, profit)
        return profit