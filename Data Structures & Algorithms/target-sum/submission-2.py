class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for n in nums:
            newdp = defaultdict(int)
            for curr_sum, count in dp.items():
                newdp[curr_sum + n] += count
                newdp[curr_sum - n] += count
            dp = newdp
        return dp[target]
