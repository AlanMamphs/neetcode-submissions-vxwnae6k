class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        increasing = []
        decreasing = []
        prev = 1
        for n in nums:
            increasing.append(prev)
            prev *= n
        prev = 1
        for n in nums[::-1]:
            decreasing.append(prev)
            prev *= n
        res = []
        N = len(nums)
        for i in range(N):
            res.append(increasing[i]*decreasing[N - i - 1])
        return res
            