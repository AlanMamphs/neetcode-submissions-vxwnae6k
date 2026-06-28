class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)

        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2

        for n in nums:
            temp = set()
            for t in dp:
                if t + n == target:
                    return True
                temp.add(t+n)
                temp.add(t)
            dp = temp
        return False