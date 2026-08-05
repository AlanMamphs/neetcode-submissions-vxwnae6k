class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        def circuit(i, tank):
            start = i
            while True:
                tank += gas[i] - cost[i]
                if tank < 0:
                    return False
                i = (i + 1) % n
                if i == start:
                    return True
            return True
        for i in range(n):
            if cost[i] <= gas[i] and circuit(i, 0):
                return i
        return -1