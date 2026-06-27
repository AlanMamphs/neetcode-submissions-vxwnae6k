class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        
        for n in nums:
            curr, prev = max(n + prev, curr), curr
        
        return max(prev, curr)