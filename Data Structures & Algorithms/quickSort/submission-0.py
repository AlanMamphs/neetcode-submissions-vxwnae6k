# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def partition(self, nums, start, end):
        pivot = nums[end]
        left = start
        for i in range(start, end):
            if nums[i].key < pivot.key:
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp
                left += 1
        
        nums[end] = nums[left]
        nums[left] = pivot

        return left

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qs(pairs, 0, len(pairs) - 1)
        return pairs

    def qs(self, nums, start, end):
        if end - start <= 0:
            return
        
        middle = self.partition(nums, start, end)
        self.qs(nums, start, middle - 1)
        self.qs(nums, middle + 1, end)
