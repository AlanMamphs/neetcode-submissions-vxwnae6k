class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        secondday = [0, 0]
        nextday = [0, 0]

        for i in range(len(prices) - 1, -1, -1):
            today = [0, 0]
            p = prices[i]
            for isbuying in (1, 0):
                skip = nextday[isbuying]
                if isbuying:
                    res = max(skip, nextday[0] - p)
                else:
                    res = max(skip, secondday[1] + p)
                today[isbuying] = res
            nextday, secondday = today, nextday
        return nextday[1]