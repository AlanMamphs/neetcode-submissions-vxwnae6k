class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(lambda: defaultdict(int))
        
        for i in range(len(prices) - 1, -1, -1):
            for isbuying in (True, False):
                cooldown = dp[i + 1][isbuying]
                if isbuying:
                    buy = dp[i+1][not isbuying] - prices[i]
                    res = max(cooldown, buy)
                else:
                    sell = dp[i + 2][not isbuying] + prices[i]
                    res = max(cooldown, sell)
                dp[i][isbuying] = res
        
        return dp[0][True]



