class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]: # mid is in left sorted array, target might be in the right though
                if nums[l] <= target < nums[mid]: # target is between left and mid
                    r = mid - 1
                else:
                    l = mid + 1
            else: # mid is in the right sorted array, target might be in the left side though
                if nums[mid] < target <= nums[r]: # target is between mid and right
                    l = mid + 1
                else:
                    r = mid - 1
        return -1