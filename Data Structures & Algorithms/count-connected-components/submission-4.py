class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        
        store = defaultdict(list)
        for i, j in edges:
            store[i].append(j)
            store[j].append(i)
        
        def dfs(i):
            visited.add(i)
            for j in store[i]:
                if j in visited:
                    continue
                dfs(j)
            return 
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
            dfs(i)
        return count

