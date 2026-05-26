class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        store = defaultdict(list)

        for u, v in edges:
            store[u].append(v)
        
        visit = dict()
        res = []
        def dfs(n):
            if n in visit:
                return not visit[n]
            visit[n] = True

            for p in store[n]:
                if not dfs(p):
                    return False
            visit[n] = False
            res.append(n)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        return res[::-1]
        
