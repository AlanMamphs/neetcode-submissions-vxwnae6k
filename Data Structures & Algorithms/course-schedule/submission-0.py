from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(set)
        for c, p in prerequisites:
            courses[c].add(p)
        
        visited = set()
        def dfs(c):
            if c in visited:
                return False
            if not courses[c]:
                return True
                
            visited.add(c)
            for p in courses[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            courses[c] = set()      
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True