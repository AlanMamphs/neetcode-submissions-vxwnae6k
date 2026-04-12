class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sublist = []
        res = []
        def backtracking(i, sublist, total):
            if target == total:
                res.append(sublist.copy())
                return

            if total > target or i >= len(candidates):
                return
            
            sublist.append(candidates[i])
            backtracking(i + 1, sublist, total + candidates[i])
            sublist.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtracking(i + 1, sublist, total)

        backtracking(0, [], 0)
        return res