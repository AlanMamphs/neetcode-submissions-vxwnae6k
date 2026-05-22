class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        flights = defaultdict(list)
        for s, d in tickets:
            flights[s].append(d)
        
        q = ['JFK']
        res = []
        while q:
            airport = q[-1]
            if flights[airport]:
                q.append(flights[airport].pop())
            else:
                res.append(q.pop())
        return res[::-1]
