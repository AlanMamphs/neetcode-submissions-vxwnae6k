class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prev = 1
        for n in nums:
            res.append(prev)
            prev *= n
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prev
            prev *= nums[i]
        return res
            