class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = dict()

        def dfs(i, curr):
            if (i, curr) in cache:
                return cache[(i, curr)]
            if i == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0
            
            res = dfs(i + 1, curr + nums[i]) + dfs(i + 1, curr - nums[i])
            cache[(i, curr)] = res
            return res
        return dfs(0, 0)