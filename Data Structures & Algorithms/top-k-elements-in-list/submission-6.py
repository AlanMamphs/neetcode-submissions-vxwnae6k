from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        for key, val in counts.items():
            buckets[val].append(key)
        
        res = []
        for items in buckets[::-1]:
            for item in items:
                if len(res) < k:
                    res.append(item)
                else:
                    return res
        return res