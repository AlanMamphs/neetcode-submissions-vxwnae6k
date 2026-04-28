class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        nums = candidates

        def dfs(i, total, curr):
            if i == len(nums) or total >= target:
                if total == target:
                    res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i+1, total + nums[i], curr)
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            curr.pop()
            dfs(i+1, total, curr)
        dfs(0, 0, [])
        return res
    


