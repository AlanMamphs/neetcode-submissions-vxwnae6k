class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: # if m is in left sorted part of array
                if nums[l] <= target < nums[m]: # target is in the left sorted part, disregard everything from the right
                    r = m - 1
                else:
                    l = m + 1
            else: # else if m is in right sorted part of the array
                if nums[m] < target <= nums[r]: # if m is in the right sorted part, disregard everything from the left
                    l = m + 1
                else:
                    r = m - 1

        return -1