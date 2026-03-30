class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            m = l + (r - l) // 2
            if nums[l] <= nums[m]:
                # we are in the left part of rotated array, we register l as min and we can discard everything from left to mid
                res = min(nums[l], res)
                l = m + 1
            else:
                # we are in the right part of rotated array, we register m as min and can discard everything from mid to right
                res = min(nums[m], res)
                r = m - 1


        return res
                