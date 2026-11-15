class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(subset, total, i):
            if total == target:
                res.append(subset.copy())
                return
            
            if total > target or i == len(nums):
                return
            
            subset.append(nums[i])
            dfs(subset, total + nums[i], i)
            subset.pop()
            dfs(subset, total, i + 1)
        
        dfs([], 0, 0)
        return res