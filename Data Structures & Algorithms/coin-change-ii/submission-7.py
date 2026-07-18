class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = defaultdict(int)
        def dfs(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
            if i == n or total > amount:
                return 0
            if total == amount:
                return 1
            res = 0
            for j in range(i, n):
                res += dfs(j, total + coins[j])
            dp[(i, total)] = res
            return res
        return dfs(0, 0)