class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2
        cache = defaultdict(bool)
        def dfs(i, t):
            if t == half:
                return True
            if i >= len(nums):
                return False
            if (i, t) in cache:
                return cache[(i, t)]
            cache[(i, t)] = dfs(i + 1, t + nums[i]) or dfs(i + 1, t)
            return cache[(i, t)]
        return dfs(0, 0)