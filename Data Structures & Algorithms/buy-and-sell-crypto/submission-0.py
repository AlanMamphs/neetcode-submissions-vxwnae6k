class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        local_min = prices[0]
        for i in range(len(prices)):
           local_min = min(prices[i], local_min)
           profit = max(profit, prices[i] - local_min)
        
        return profit
