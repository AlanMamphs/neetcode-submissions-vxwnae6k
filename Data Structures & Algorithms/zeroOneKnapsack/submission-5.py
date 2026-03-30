class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        prev = [0 if x < weight[0] else profit[0] for x in range(capacity + 1)]
        print(prev)
        for i in range(1, len(profit)):
            curr = [0] * (capacity + 1)
            w = weight[i]
            p = profit[i]
            for c in range(1, capacity + 1):
                mp = prev[c]
                if w <= c:
                    mp = max(mp, p + prev[c - w])
                curr[c] = mp
            prev = curr
            print(prev)
        return prev[-1]