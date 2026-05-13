class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        edges = defaultdict(list)
        for origin, destination in tickets:
            edges[origin].append(destination)
        
        res = ['JFK']

        def dfs(origin):
            print(origin, res)
            if len(res) == len(tickets) + 1:
                return True
            if not edges[origin]:
                return False

            for i in range(len(edges[origin])):
                dest = edges[origin].pop(i)
                res.append(dest)
                if dfs(dest):
                    return True
                edges[origin].insert(i, res.pop())
            return False
        dfs('JFK')
        return res


