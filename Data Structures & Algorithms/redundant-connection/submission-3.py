class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pars = [i for i in range(len(edges) + 2)]
        rank = [1] * (len(edges) + 2)

        def find(n):
            if n != pars[n]:
                pars[n] = find(pars[n])
            return pars[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                pars[p2] = p1
                rank[p1] += rank[p2]
            else:
                pars[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
