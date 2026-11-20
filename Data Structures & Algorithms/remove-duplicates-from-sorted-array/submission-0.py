class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0

        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
            r += 1

        return l + 1


