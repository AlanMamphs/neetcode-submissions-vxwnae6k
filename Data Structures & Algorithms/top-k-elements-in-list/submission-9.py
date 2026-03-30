from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq) - 1, -1, -1):
            for el in freq[i]:
                if len(res) < k:
                    res.append(el)
                else:
                    break
        return res

