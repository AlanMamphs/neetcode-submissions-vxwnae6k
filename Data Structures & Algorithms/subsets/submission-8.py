class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            res = res + [x + [n] for x in res]
        return res