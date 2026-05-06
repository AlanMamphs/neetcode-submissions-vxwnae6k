class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        store = defaultdict(set)
        for n1, n2 in edges:
            store[n1].add(n2)
            store[n2].add(n1)
        
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for p in store[i]:
                if p == prev:
                    continue
                dfs(p, i)
            return True

        res = 0
        for i in range(n):
            prev = len(visited)
            dfs(i, -1)
            if len(visited) != prev:
                res += 1
        return res
