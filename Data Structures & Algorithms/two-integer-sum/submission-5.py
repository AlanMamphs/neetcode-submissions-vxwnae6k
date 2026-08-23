class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for i in range(len(nums)):
            n = nums[i]
            m = target - n
            if m in map:
                return [map[m], i]
            map[n] = i
        return False