class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(i, sublist):
            if i >= len(nums):
                res.append(sublist.copy())
                return
            sublist.append(nums[i])
            backtracking(i + 1, sublist)
            sublist.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtracking(i + 1, sublist)
        backtracking(0, [])
        return res