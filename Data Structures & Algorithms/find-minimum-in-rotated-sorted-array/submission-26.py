class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                if nums[m] < nums[r]: # we are in the right side
                    r = m
                else: # we are in the left side
                    l = m + 1
        return nums[l]