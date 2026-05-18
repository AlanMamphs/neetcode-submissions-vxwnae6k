class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        
        flights = defaultdict(list)
        for src, dst in tickets:
            flights[src].append(dst)

        q = ['JFK']
        res = []
        while q:
            if not flights[q[-1]]:
                res.append(q.pop())
            else:
                q.append(flights[q[-1]].pop())
        return res[::-1]
            

