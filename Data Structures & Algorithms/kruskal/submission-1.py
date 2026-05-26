class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: x[2])

        pars = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(n):
            if pars[n] != n:
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
        res = 0
        visit = set()
        for u, v, w in edges:
            if union(u, v):
                res += w
                visit.add((u, v))
                
            
        return -1 if n -1 != len(visit)else res
