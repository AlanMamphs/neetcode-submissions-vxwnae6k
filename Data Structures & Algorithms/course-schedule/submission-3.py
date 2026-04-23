class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        courses = defaultdict(list)

        for c, p in prerequisites:
            courses[c].append(p)

        def dfs(c):
            if c in visited:
                return False
            if not courses[c]:
                return True
            
            visited.add(c)

            for p in courses[c]:
                if not dfs(p):
                    return False
            courses[c] = []
            visited.remove(c)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True