class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = defaultdict(bool)
        coins.sort()
        res = 0
        def dfs(i, target):
            if target == 0:
                return 1
            if (i, target) in cache:
                return cache[(i, target)]
            if target < 0 or i == len(coins):
                return 0
            res = 0
            for j in range(i, len(coins)):
                res += dfs(j, target - coins[j])
            cache[(i, target)] = res
            return res
        return dfs(0, amount)
        



