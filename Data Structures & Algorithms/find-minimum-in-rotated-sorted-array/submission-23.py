class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        res = nums[0]

        while l <= r:
            m = l + (r - l) // 2

            res = min(res, nums[l])
            if nums[l] <= nums[m]:
                # in the left sorted side of the array. register minimum (left) and search in right part
                res = min(res, nums[l])
                l = m + 1
            else:
                # in the right sorted side of the array. register minimum (mid) and search in left part
                res = min(res, nums[m])
                r = m - 1
        return res