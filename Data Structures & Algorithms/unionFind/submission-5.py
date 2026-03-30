class UnionFind:
    
    def __init__(self, n: int):
        self.pars = {}
        self.rank = {}
        self.num_components = n

        for i in range(n):
            self.pars[i] = i
            self.rank[i] = 0
        

    def find(self, x: int) -> int:
        p = self.pars[x]

        while p != self.pars[p]:
            self.pars[p] = self.pars[self.pars[p]]
            p = self.pars[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.pars[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.pars[p1] = p2
        else:
            self.pars[p1] = p2
            self.rank[p1] += 1
        self.num_components -= 1
        return True        

    def getNumComponents(self) -> int:
        return self.num_components
