class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sublist = []
        nums.sort()

        def backtracking(i, sublist, total):
            if total == target:
                res.append(sublist.copy())
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                sublist.append(nums[j])
                backtracking(j, sublist, total + nums[j])
                sublist.pop()
        backtracking(0, [], 0)
        return res