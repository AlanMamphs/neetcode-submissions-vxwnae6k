class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(int)
        for i in range(len(prices) -1, -1, -1):
            for isbuying in (True, False):
                skip = dp[(i+1, isbuying)]
                if isbuying:
                    buy = dp[(i+1, False)] - prices[i]
                    res = max(skip, buy)
                else:
                    sell = dp[(i+2, True)] + prices[i]
                    res = max(skip, sell)
                dp[(i, isbuying)] = res
        return dp[(0, True)]