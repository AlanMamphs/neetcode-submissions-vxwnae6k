class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = {0}
        res = 0
        while q:
            temp = set()
            for a in q:
                if a == amount:
                    return res
                for c in coins:
                    na = a + c
                    if na <= amount:
                        temp.add(na)
            q = temp
            res += 1
        return -1