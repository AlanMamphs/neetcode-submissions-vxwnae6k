from collections import defaultdict, deque

class Graph:
    
    def __init__(self):
        self.data = defaultdict(list)

    def addEdge(self, src: int, dst: int) -> None:
        self.data[src].append(dst)
        self.data[dst] += []
        print(self.data)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.data or dst not in self.data:
            return False
        
        if len(self.data[dst]) == 0:
            del self.data[dst]
        
        try:
            self.data[src].remove(dst)
            return True
        except:
            return False
        
    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.data or dst not in self.data:
            return False
        
        stack = deque([src])
        visited = set()
        while stack:
            el = stack.popleft()
            visited.add(el)
            if el == dst:
                return True
            stack.extend([x for x in self.data[el] or [] if x not in visited])
        return False
