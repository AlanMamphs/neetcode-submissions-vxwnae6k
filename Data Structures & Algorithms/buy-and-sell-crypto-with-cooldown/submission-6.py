class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(lambda: defaultdict(int))

        n = len(prices)

        for i in range(n - 1, -1, -1):
            for isbuying in (True, False):
                if isbuying:
                    buy = dp[i+1][False] - prices[i]
                    skip = dp[i+1][True]
                    dp[i][True] = max(buy, skip)
                else:
                    sell = dp[i+2][True] + prices[i]
                    skip = dp[i+1][False]
                    dp[i][False] = max(sell, skip)
        return dp[0][True]
                