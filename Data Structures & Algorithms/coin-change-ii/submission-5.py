class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = dict()
        coins.sort()
        res = defaultdict

        def dfs(i, amount):
            if (i, amount) in cache:
                return cache[(i, amount)]
            
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            
            res = 0

            for j in range(i, len(coins)):
                c = coins[j]
                if amount < c:
                    break
                res += dfs(j, amount - c)
            cache[(i, amount)] = res
            return res
        return dfs(0, amount)
            

            
            