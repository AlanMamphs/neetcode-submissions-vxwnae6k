class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        store = defaultdict(set)
        for n1, n2 in edges:
            store[n1].add(n2)
            store[n2].add(n1)
        
        def dfs(i, prev):
            
            visited.add(i)
            for p in store[i]:
                if p == prev or p in visited:
                    continue
                if not dfs(p, i):
                    return False
            return True

        res = 0
        for i in range(n):
            prev = len(visited)
            dfs(i, -1)
            if len(visited) != prev:
                res += 1
        return res
