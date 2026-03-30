class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            val = nums[i]
            remainder = target - val
            if remainder in cache:
                return [cache[remainder], i]
            cache[val] = i

        