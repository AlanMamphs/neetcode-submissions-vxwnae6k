class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pars = [n for n in range(len(edges) + 1)]
        rank = [1 for n in range(len(edges) + 1)]
        
        def find_root(n):
            if n != pars[n]:
                pars[n] = find_root(pars[n])
            return pars[n]
        
        def union(n1, n2):
            p1, p2 = find_root(n1), find_root(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                pars[p2] = p1
                rank[p1] += rank[p2]
            else:
                pars[p1] = p2
                rank[p2] = rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


        