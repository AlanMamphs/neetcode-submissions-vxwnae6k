class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(subset, total, i):
            if target == total:
                res.append(subset.copy())
                return
            if total > target or i == len(candidates):
                return
            subset.append(candidates[i])
            dfs(subset, total + candidates[i], i + 1)
            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            subset.pop()
            dfs(subset, total, i + 1)
            return
        dfs([], 0, 0)
        return res

