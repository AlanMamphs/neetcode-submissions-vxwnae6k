class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        store = defaultdict(set)

        for a, b in edges:
            store[a].add(b)
            store[b].add(a)

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in store[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, float('-inf')) and len(visited) == n