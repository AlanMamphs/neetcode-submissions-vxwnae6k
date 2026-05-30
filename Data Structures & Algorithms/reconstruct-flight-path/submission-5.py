class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        routes = defaultdict(list)
        for src, dst in tickets:
            routes[src].append(dst)
        res = ['JFK']

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if not routes[src]:
                return False
            
            for i in range(len(routes[src])):
                res.append(routes[src].pop(i))
                if dfs(res[-1]):
                    return True
                routes[src].insert(i, res.pop())
            return False
        dfs('JFK')
        return res