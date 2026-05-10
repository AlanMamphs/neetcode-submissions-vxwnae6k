class Solution:
    def rob(self, nums: List[int]) -> int:
        store = dict()
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in store:
                return store[i]
            include = dfs(i + 2) +  nums[i]
            skip = dfs(i + 1)
            store[i] = max(include, skip)
            return store[i]
        return dfs(0)
            
        