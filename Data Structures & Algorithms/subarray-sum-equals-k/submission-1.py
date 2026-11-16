class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] += 1
        prefix = 0
        res = 0
        for n in nums:
            prefix += n
            res += prefix_sum[prefix - k]
            prefix_sum[prefix] += 1
        return res