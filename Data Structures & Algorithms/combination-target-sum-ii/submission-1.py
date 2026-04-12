class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtracking(i, sublist, total):
            if target == total:
                res.append(sublist.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] + total > target:
                    return
                sublist.append(candidates[j])
                backtracking(j + 1, sublist, total + candidates[j])
                sublist.pop()
        backtracking(0, [], 0)
        return res