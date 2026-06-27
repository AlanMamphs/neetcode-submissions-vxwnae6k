class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        _min, _max = 1, 1
        for n in nums:
            nmin = _min * n
            nmax = _max * n
            _min = min(n, nmin, nmax)
            _max = max(n, nmin, nmax)
            res = max(_max, res)
        return res