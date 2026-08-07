class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)
        
        curr = defaultdict(int)
        remaining = 0
        res = []
        for c in s:
            if c not in curr:
                remaining += counts[c]
            curr[c] += 1
            remaining -= 1
            if remaining == 0:
                res.append(sum(curr.values()))
                curr = defaultdict(int)
        return res
