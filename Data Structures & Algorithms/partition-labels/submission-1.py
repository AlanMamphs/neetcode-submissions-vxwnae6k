class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = dict()
        for i, c in enumerate(s):
            last_index[c] = i
        
        res = []
        end = 0
        size = 0
        for i, c in enumerate(s):
            end = max(end, last_index[c])
            size += 1
            
            if end == i:
                res.append(size)
                size = 0
        return res




