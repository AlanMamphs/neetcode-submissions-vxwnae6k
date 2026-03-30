# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def partition(self, pairs, start, end):
        pivot = pairs[end].key

        l = start
        for i in range(start, end):
            if pairs[i].key < pivot:
                pairs[l], pairs[i] = pairs[i], pairs[l]
                l += 1
        pairs[l], pairs[end] = pairs[end], pairs[l]
        return l
        
    def helper(self, pairs, start, end):
        if start >= end:
            return pairs
        pivot = self.partition(pairs, start, end)
        self.helper(pairs, start, pivot - 1)
        self.helper(pairs, pivot+1, end)
        return pairs


    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.helper(pairs, 0, len(pairs) - 1)        
