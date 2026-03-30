from collections import defaultdict

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        res = 1
        stack = []
        for i, (p, s) in sorted(enumerate(zip(position, speed)), key=lambda x: x[1], reverse=True):
            time = (target - p) / s
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
              stack.append(time)
            
        return len(stack)

        # Input: target = 10, position = [1,4], speed = [3,2]
        #    4 6 8 10
        # 1  4  7  10 
        #
        # target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        # 1|0123
        # 2| 1 3 5 7
        # 2|    4 6 8 10
        # 1|       78910

        # [(7, 3), (4, 3), (1, 4.5), (0, 10)]