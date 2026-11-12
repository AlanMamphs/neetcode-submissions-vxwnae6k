class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def dfs(curr, i):
            if i == len(nums):
                subsets.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(curr, i + 1)
            curr.pop()
            dfs(curr, i + 1)
            return
        dfs([], 0)
        return subsets