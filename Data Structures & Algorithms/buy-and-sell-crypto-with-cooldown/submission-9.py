class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(lambda: defaultdict(int))
        cache = dict()
        def dfs(i, isbuying):
            if (i, isbuying) in cache:
                return cache[(i, isbuying)]
            if len(prices) <= i:
                return 0
            
            if isbuying:
                cooldown = dfs(i + 1, isbuying)
                buy = dfs(i + 1, not isbuying) - prices[i]
                res = max(cooldown, buy)
            else:
                cooldown = dfs(i + 1, isbuying)
                sell = dfs(i + 2, not isbuying) + prices[i]
                res = max(cooldown, sell)
            cache[(i, isbuying)] = res
            return res
        return dfs(0, True)



