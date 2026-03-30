from pprint import pprint
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        prev = [profit[0] if weight[0] <= c else 0 for c in range(capacity + 1)]
        pprint(prev)
        for i in range(1, len(profit)):
            curr = [0] * (capacity + 1)
            for c in range(1, capacity + 1):
                max_profit = prev[c]
                include = 0
                if weight[i] <= c:
                    include = profit[i] + prev[c - weight[i]]
                
                curr[c] = max(max_profit, include)
            prev = curr
            pprint(prev)
        return prev[capacity]