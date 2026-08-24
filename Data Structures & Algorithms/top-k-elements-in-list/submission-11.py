class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        freq = defaultdict(list)
        for num, count in counts.items():
            freq[count].append(num)
        
        res = []

        for i in range(len(nums), -1, -1):
            if freq[i]:
                res.extend(freq[i])
            if len(res) >= k:
                break
        return res[:k]