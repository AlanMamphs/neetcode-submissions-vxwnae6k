class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        dp = dict()

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            res = 0
            for i in range(l, r + 1):
                curr = nums[l - 1] * nums[i] * nums[r + 1]
                left = dfs(l, i - 1)
                right = dfs(i + 1, r)
                res = max(res, left + curr + right)
            dp[(l, r)] = res
            return res
        
        return dfs(1, len(nums) - 2)