from pprint import pprint
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        grid = [[0] * (capacity + 1) for _ in range(len(profit))]
        for i in range(min(weight[0], capacity + 1), capacity + 1):
            grid[0][i] = profit[0]
        pprint(grid)

        for i in range(1, len(profit)):
            for c in range(1, capacity + 1):
                max_profit = grid[i-1][c]
                include = 0
                if weight[i] <= c:
                    include = profit[i] + grid[i - 1][c - weight[i]]
                grid[i][c] = max(max_profit, include)
        pprint(grid)
        return grid[len(profit) - 1][capacity]