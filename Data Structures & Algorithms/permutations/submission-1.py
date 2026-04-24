class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, visited):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    curr.append(nums[i])
                    dfs(curr,visited)
                    curr.pop()
                    visited.remove(i)
        dfs([], set())
        return res


