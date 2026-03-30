class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            m = l + (r - l) // 2
            res = min(nums[m], res)
            if nums[l] < nums[r]: # we are in the sorted array
                res = min(nums[l], res)
                break # no rotation between l and r

            # there is certainly a rotation 
            if nums[l] <= nums[m]:
                # we are in the left part of rotated array, and we can discard everything from left to mid
                l = m + 1
            else:
                # we are in the right part of rotated array, we can discard everything from mid to right
                r = m - 1

        return res
                