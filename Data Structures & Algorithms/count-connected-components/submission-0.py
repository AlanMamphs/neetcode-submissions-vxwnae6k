class UnionFind:
    def __init__(self, n):
        self.num_components = n
        self.pars = []
        self.rank = []
        for i in range(n):
            self.pars.append(i)
            self.rank.append(1)
        
    def findRoot(self, x):
        p = self.pars[x]
        while p != self.pars[p]:
            self.pars[p] = self.pars[self.pars[p]]
            p = self.pars[p]
        return p

    def union(self, x, y):
        p1, p2 = self.findRoot(x), self.findRoot(y)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.pars[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.pars[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.num_components -= 1
        return True
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        
        return uf.num_components
