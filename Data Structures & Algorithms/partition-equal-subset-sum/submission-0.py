class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)
        total = sum(nums)
        target = total // 2
        if total % 2:
            return False
        
        for n in nums:
            new = set()
            for t in dp:
                if t + n == target:
                    return True
                new.add(t+n)
                new.add(t)
            dp = new
        return False