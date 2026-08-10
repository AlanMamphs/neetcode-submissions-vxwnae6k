class Solution:
    def jump(self, nums: List[int]) -> int:
        right_max = 0
        goal = len(nums) - 1
        l = 0
        r = 0
        res = 0
        while r < goal:
            for i in range(l, r + 1):
                right_max = max(right_max, i + nums[i])
            l = r
            r = right_max
            res += 1
        
        return res
        