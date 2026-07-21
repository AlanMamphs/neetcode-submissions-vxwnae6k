class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()
        def dfs(i, isbuying):
            if (i, isbuying) in dp:
                return dp[(i, isbuying)]
            if i >= len(prices):
                return 0
            skip = dfs(i+1, isbuying)
            if isbuying:
                buy = dfs(i+1, False) - prices[i]
                res = max(skip, buy)
            else:
                sell = dfs(i+2, True) + prices[i]
                res = max(skip, sell)
            dp[(i, isbuying)] = res
            return res
        return dfs(0, True)