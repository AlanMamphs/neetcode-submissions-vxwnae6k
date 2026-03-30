from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        print(count)
        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets)
        for i, v in count.items():
            buckets[v].append(i)
        print(buckets)
        result = []
        for i in range(len(nums), 0, -1):
            if buckets[i]:
                result.extend(buckets[i])
            
            if len(result) >= k:
                return result[:k]

        return result