class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        store = defaultdict(list)
        for i, j in edges:
            store[i].append(j)
            store[j].append(i)
    
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for j in store[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, float('-inf')) and len(visited) == n