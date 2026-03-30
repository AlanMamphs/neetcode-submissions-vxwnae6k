class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                # there is still rotation and we are in the left part
                # in this case we can discard left part completely, 
                # because the min is in the right part
                l = m + 1
            else:
                # there might be no rotation, or we are in the right part of it right now
                # safely move the right pointer to mid as it is the fartherst we can go
                r = m

        return nums[l]

        # [3, 4, 5, 1, 2]