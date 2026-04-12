class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, res = [], []
        def backtracking(i, subsets):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            subsets.append(nums[i])
            backtracking(i + 1, subsets)
            subsets.pop()
            backtracking(i + 1, subsets)
        
        backtracking(0, subsets)

        return res
            

