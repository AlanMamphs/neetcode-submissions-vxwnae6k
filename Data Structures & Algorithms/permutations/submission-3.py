class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, visited):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for j in range(len(nums)):
                if nums[j] in visited:
                    continue
                visited.add(nums[j])
                curr.append(nums[j])
                dfs(curr, visited)
                curr.pop()
                visited.remove(nums[j])
        dfs([], set())
        return res