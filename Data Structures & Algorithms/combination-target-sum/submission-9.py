class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(subset, pre, i):
            if i == len(nums) or pre > target:
                return
            if pre == target:
                res.append(subset.copy())
                return       
            subset.append(nums[i])
            dfs(subset, pre + nums[i], i)
            subset.pop()
            dfs(subset, pre, i + 1)
        dfs([], 0, 0)
        return res
