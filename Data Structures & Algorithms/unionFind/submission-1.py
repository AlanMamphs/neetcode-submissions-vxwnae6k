class UnionFind:
    
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.rank = [1] * n
        self.num_components = n

    def find(self, x: int) -> int:
        parent = self.parents[x]
        grand_parent = self.parents[parent]
        while parent != grand_parent:
            grand_parent = self.parents[grand_parent]
            self.parents[parent] = grand_parent
            parent = self.parents[parent]
        
        return parent

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parents[p1] = p2
        else:
            self.rank[p1] += 1
            self.parents[p2] = p1
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components
