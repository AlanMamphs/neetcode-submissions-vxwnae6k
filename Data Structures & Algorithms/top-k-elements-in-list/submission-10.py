class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        return [k for k, count in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:k]]
