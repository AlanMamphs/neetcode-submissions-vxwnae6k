class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for src, dst in tickets:
            adj[src].append(dst)
        
        q = ['JFK']
        res = []
        while q:
            if adj[q[-1]]:
                q.append(adj[q[-1]].pop())
            else:
                res.append(q.pop())
        return res[::-1]