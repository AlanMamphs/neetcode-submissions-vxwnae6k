class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = dict()

        def dfs(i, canbuy):
            if (i, canbuy) in cache:
                return cache[(i, canbuy)]

            if i >= len(prices):
                return 0
            # skip
            res = dfs(i + 1, canbuy)
            if canbuy:
                res = max(res, dfs(i + 1, False)  - prices[i])
            else:
                res = max(res, dfs(i + 2, True) + prices[i])
            cache[(i, canbuy)] = res
            return res
        return dfs(0, True)