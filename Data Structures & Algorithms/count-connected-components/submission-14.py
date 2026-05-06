class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        store = defaultdict(set)
        for n1, n2 in edges:
            store[n1].add(n2)
            store[n2].add(n1)
        
        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            for p in store[i]:
                dfs(p)
            return True

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
