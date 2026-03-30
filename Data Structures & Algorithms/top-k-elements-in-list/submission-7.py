from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1
        
        most_freq = sorted([(v, k) for k, v in count.items()], reverse=True)
        return [x[1] for x in most_freq[:k]]

