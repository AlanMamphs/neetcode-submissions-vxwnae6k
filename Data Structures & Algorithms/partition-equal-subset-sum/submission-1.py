class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2

        def dfs(i, t):
            if t == half:
                return True
            if i >= len(nums):
                return False
            if dfs(i + 1, t + nums[i]) or dfs(i + 1, t):
                return True
            return False
        return dfs(0, 0)