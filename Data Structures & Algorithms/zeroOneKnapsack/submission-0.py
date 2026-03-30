class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        cache = {}
        def dfs_helper(i, curr_weight):
            if i == N:
                return 0
            if cache.get((i, curr_weight)):
                return cache[(i, curr_weight)]
            # skip
            max_profit = dfs_helper(i + 1, curr_weight)
            if curr_weight + weight[i] <= capacity:
                # include
                max_profit = max(max_profit, profit[i] + dfs_helper(i + 1, curr_weight + weight[i]))
            cache[(i, curr_weight)] = max_profit
            return max_profit
        
        return dfs_helper(0, 0)