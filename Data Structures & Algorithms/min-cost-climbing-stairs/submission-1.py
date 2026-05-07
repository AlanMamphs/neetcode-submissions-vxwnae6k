class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        curr = 0
        prev = 0
        for i in range(n - 1, -1, -1):
            tmp = curr
            curr = min(prev, curr) + cost[i]
            prev = tmp
        
        return min(curr, prev)
