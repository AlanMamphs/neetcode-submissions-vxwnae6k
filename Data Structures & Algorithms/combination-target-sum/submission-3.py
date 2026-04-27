class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, total, curr):
            if i == len(nums) or total > target:
                return
            if total == target:
                res.append(curr.copy())
                return
            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j, total + nums[j], curr)
                curr.pop()
        dfs(0, 0, [])
        return res