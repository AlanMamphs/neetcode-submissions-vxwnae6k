class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        c = 1
        for d in digits[::-1]:
            c, r = divmod((d+c), 10)
            res.append(r)
        
        if c:
            res.append(c)
        
        return res[::-1]

