class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if l == r:
                return nums[l]
            m = l + (r - l) // 2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m + 1
        