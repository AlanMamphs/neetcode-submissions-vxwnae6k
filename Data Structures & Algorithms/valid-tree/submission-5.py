class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        visited = set()
        store = defaultdict(set)
        
        for n1, n2 in edges:
            store[n1].add(n2)
            store[n2].add(n1)
        
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)

            for child in store.get(i) or []:
                if child == prev:
                    continue
                if not dfs(child, i):
                    return False
            return True
        
        
        return dfs(1, -1) and len(visited) == n