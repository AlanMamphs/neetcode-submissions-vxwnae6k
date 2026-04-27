class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        res = []

        def dfs(i, total, curr):
            if total == target:
                res.append(curr.copy())
                return

            if i == len(nums) or total > target:
                return
            curr.append(nums[i])
            dfs(i + 1, total + nums[i], curr)
            curr.pop()
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i + 1, total, curr)

        
        dfs(0, 0, [])
        return res