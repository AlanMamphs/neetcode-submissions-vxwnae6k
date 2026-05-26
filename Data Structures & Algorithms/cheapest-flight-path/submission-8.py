class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        edges = defaultdict(list)

        for i in range(k + 1):
            temp = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                temp[d] = min(prices[s] + p, temp[d])
            prices = temp
        return -1 if float('inf') == prices[dst] else prices[dst]