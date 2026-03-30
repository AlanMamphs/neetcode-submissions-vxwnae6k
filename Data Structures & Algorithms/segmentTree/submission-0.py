class Node:
    def __init__(self, l, r, v = 0, L = None, R = None):
        self.l = l
        self.r = r
        self.v = v
        self.L = L
        self.R = R
    
    @classmethod
    def build(cls, l, r, nums):
        n = cls(l, r)
        if l == r:
            n.v = nums[l]
            return n
        
        M = (l + r) // 2

        n.L = cls.build(l, M, nums)
        n.R = cls.build(M + 1, r, nums)
        n.v = n.L.v + n.R.v
        return n
    
    def update(self, index, val):
        M = (self.l + self.r) // 2
        
        if index == self.l == self.r:
            self.v = val
            return self

        if index <= M:
            self.L.update(index, val)
        else:
            self.R.update(index, val)
        
        self.v = self.L.v + self.R.v

        return self

    def query(self, L, R):
        M = self.l + (self.r - self.l) // 2
        if L == self.l and R == self.r:
            return self.v

        if R <= M:
            return self.L.query(L, R)
        elif L > M:
            return self.R.query(L, R)
        
        return self.L.query(L, M) + self.R.query(M + 1, R)


class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = Node.build(0, len(nums) - 1, nums)
    
    def update(self, index: int, val: int) -> None:
        self.root.update(index, val)
    
    def query(self, L: int, R: int) -> int:
        return self.root.query(L, R)
