class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = dict()

        def dfs(i, profit, canbuy):
            if (i, profit, canbuy) in cache:
                return cache[(i, profit, canbuy)]

            if i >= len(prices):
                return profit
            # skip
            res = dfs(i + 1, profit, canbuy)
            if canbuy:
                res = max(res, dfs(i + 1, profit - prices[i], False))
            else:
                res = max(res, dfs(i + 2, profit + prices[i], True))
            cache[(i, profit, canbuy)] = res
            return res
        return dfs(0, 0, True)