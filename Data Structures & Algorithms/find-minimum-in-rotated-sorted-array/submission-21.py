class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        res = nums[0]

        while l <= r:
            m = l + (r - l) // 2

            if nums[l] <= nums[m]:
                res = min(res, nums[l])
                l = m + 1
            else:
                res = min(res, nums[m])
                r = m - 1
        return res