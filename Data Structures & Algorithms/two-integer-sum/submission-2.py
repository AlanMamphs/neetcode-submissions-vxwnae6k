class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, n in enumerate(nums):
            print(index)
            if (j := (target - n)) in index:
                return sorted([i, index[j]])
            index[n] = i
        