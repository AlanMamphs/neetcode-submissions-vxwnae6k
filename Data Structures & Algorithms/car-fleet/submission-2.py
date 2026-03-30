from collections import defaultdict

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        res = 0
        prev = None
        for i, (p, s) in sorted(enumerate(zip(position, speed)), key=lambda x: x[1], reverse=True):
            time = (target - p) / s
            if not prev:
                res += 1
                prev = time
            elif time > prev:
                res += 1
                prev = time
            
        return res