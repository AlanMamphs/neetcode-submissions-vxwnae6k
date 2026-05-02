class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, total, curr):
            if i == len(nums) or total >= target:
                if total == target:
                    res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i, total + nums[i], curr)
            curr.pop()
            dfs(i + 1, total, curr)
        dfs(0, 0, [])
        return res