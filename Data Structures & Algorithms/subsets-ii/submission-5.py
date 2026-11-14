class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(subset, i):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(subset, i + 1)
            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            subset.pop()
            dfs(subset, i + 1)
        dfs([], 0)
        return res