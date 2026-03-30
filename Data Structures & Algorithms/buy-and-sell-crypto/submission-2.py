class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest = prices[0]
        for r in range(len(prices)):
            profit = max(profit, prices[r] - cheapest)
            cheapest = min(cheapest, prices[r])
        
        return profit
