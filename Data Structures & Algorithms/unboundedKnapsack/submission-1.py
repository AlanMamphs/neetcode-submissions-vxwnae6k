class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        prev = [0] * (capacity + 1)

        for i in range(len(profit)):
            curr = [0] * (capacity + 1)
            p = profit[i]
            w = weight[i]
            for c in range(1, capacity + 1):
                if w <= c:
                    curr[c] = max(prev[c], curr[c - w] + p)
                else:
                    curr[c] = prev[c]
            prev = curr
        
        return prev[-1]