class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):
            if (j := target - nums[i]) in memo:
                return [memo[j], i]         
            memo[nums[i]] = i
