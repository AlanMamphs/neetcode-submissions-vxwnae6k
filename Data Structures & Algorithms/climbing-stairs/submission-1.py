class Solution:
    def climbStairs(self, n: int) -> int:
        res = []
        mem = defaultdict(int)

        mem[2] = 2
        mem[1] = 1
        mem[0] = 0

        def dfs(total):
            if total < 0:
                return
            if total in mem:
                return mem[total]
            mem[total] = dfs(total - 1) + dfs(total - 2)
            return mem[total]
        
       
        return dfs(n)
