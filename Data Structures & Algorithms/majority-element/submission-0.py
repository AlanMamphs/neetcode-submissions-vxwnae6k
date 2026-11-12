class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        target = len(nums) / 2

        for n in nums:
            counts[n] += 1
            if counts[n] >= target:
                return n