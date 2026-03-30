from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        roots = defaultdict(int)
        result = 0
        for i in nums:
            if (i - 1) not in nums:
                curr = i
                while curr in nums:
                    roots[i] += 1
                    curr += 1
                result = max(result, roots[i])

        return result        