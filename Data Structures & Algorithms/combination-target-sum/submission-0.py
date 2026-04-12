class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets, res = [], []
        def backtracking(i, sum_s_f, subsets):
            if i >= len(nums) or sum_s_f >= target:
                if sum_s_f == target:
                    res.append(subsets.copy())
                return
            subsets.append(nums[i])
            backtracking(i, sum_s_f + nums[i], subsets)
            subsets.pop()
            backtracking(i + 1, sum_s_f, subsets)

        backtracking(0, 0, subsets)
        return res      