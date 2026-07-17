class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [defaultdict(int) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for isbuying in (True, False):
                cooldown = dp[i + 1][isbuying]
                if isbuying:
                    buy = dp[i + 1][False] - prices[i]
                    dp[i][True] = max(cooldown, buy)
                else:
                    sell = i + 2 <= n and dp[i + 2][True] + prices[i] or prices[i]
                    dp[i][False] = max(cooldown, sell)

        return dp[0][True]