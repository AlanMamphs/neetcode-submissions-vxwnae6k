class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        courses = defaultdict(list)

        for c, p in prerequisites:
            courses[c].append(p)
        
        res = dict()
        def dfs(c):
            if c in visited:
                return False
            if not courses[c]:
                res[c] = True
                return True
            visited.add(c)
            for p in courses[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            courses[c] = []
            res[c] = True
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return list(res.keys())
