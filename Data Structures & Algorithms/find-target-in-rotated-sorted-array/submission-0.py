class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            v = nums[mid]
            if target == v:
                return mid
            
            if nums[l] <= v:
                if v < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[r] < target or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

            # 3, 4, 5, 6, 1,  2