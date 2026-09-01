class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[l] <= nums[m] <= nums[r]: # sorted array
                return nums[l]
            
            if nums[r] < nums[l] <= nums[m]:
                # we are in left unsorted part
                l = m + 1
            elif nums[m] <= nums[r] <= nums[l]:
                r = m
        return nums[l]
