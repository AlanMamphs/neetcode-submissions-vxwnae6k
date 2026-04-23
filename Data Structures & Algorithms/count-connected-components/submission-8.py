class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        store = defaultdict(set)

        for a, b in edges:
            store[a].add(b)
            store[b].add(a)
        
        def dfs(node):
            visited.add(node)
            for adjacent in store[node]:
                if adjacent in visited:
                    continue
                dfs(adjacent)
        
        count = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            count += 1

        return count