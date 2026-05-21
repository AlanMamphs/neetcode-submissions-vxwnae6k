class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        edges = defaultdict(list)
        for s, d, p in flights:
            edges[s].append((d, p))

        q = [(0, src, 0)]
        while q:
            tmp = []
            for p, s, stops in q:
                if stops > k:
                    continue
                for d, p2 in edges[s]:
                    new_cost = p + p2
                    if new_cost < prices[d]:
                        prices[d] = new_cost
                        tmp.append((new_cost, d, stops + 1))
            q = tmp
        return prices[dst] if prices[dst] != float('inf') else -1
