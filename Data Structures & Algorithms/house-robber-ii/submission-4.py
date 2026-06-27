class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(sub):
            prev, curr = 0, 0

            for n in sub:
                curr, prev = max(n + prev, curr), curr
            
            return max(curr, prev)
        
        return max(nums[0], _rob(nums[1:]), _rob(nums[:-1]))