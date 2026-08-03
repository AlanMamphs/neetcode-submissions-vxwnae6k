class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n  = len(nums)
        nums = [1] + nums + [1]

        cache = dict()

        def dfs(l, r):
            if (l, r) in cache:
                return cache[(l, r)]
            
            if l > r:
                return 0
            res = 0
            for i in range(l, r + 1):
                burst_last = nums[l - 1] * nums[i] * nums[r + 1]
                res = max(res, dfs(l, i - 1) + burst_last + dfs(i + 1, r))
            cache[(l, r)] = res
            return res
        
        return dfs(1, n)