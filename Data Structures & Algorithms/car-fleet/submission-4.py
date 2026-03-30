from collections import defaultdict

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        res = 1
        prev = None
        for p, s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            if not prev:
                prev = time
            elif time > prev:
                res += 1
                prev = time
            
        return res