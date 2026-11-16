class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        n_3 = len(nums) / 3

        res = set()

        for n in nums:
            counts[n] += 1
            if counts[n] > n_3:
                res.add(n)
        return list(res)
            