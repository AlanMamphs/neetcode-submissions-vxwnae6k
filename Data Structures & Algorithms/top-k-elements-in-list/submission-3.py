from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for i, v in count.items():
            buckets[v].append(i)
        result = []
        for i in range(len(nums), 0, -1):
            if buckets[i]:
                result.extend(buckets[i])
            
            if len(result) >= k:
                return result[:k]

        return result