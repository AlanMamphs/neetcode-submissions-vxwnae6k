class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = defaultdict(list)
        for s, d in tickets:
            adj[s].append(d)
        q = ['JFK']
        res = []
        while q:
            if adj[q[-1]]:
                q.append(adj[q[-1]].pop())
            else:
                res.append(q.pop())
        return res[::-1]