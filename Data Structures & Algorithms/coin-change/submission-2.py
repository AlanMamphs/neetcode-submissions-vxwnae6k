class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = set([amount])
        res = 0
        coins.sort(reverse=True)
        while q:
            temp = set()
            for a in q:
                if a == 0:
                    return res
                
                for c in coins:
                    na = a - c
                    if na == 0:
                        return res + 1
                    if na > 0:
                        temp.add(na)
                    
            res += 1
            q = temp
            
        return -1
