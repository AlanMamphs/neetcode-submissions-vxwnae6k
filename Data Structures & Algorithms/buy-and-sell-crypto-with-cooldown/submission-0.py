class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = dict()

        def dfs(i, can_buy):
            if (i, can_buy) in cache:
                return cache[(i, can_buy)]
            if i >= len(prices):
                return 0
            
            cooldown = dfs(i + 1, can_buy)
            if can_buy:
                profit = dfs(i + 1, False) - prices[i]
            else:
                profit = dfs(i + 2, True) + prices[i]
            cache[(i, can_buy)] = max(profit, cooldown)

            return cache[(i, can_buy)]
        
        return dfs(0, True)


