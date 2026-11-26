class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a < 0:
                
                while stack and stack[-1] > 0 and (stack[-1] + a) < 0:
                    stack.pop()
                if stack and stack[-1] > 0 and (stack[-1] + a) >= 0:
                    if (stack[-1] + a) == 0:
                        stack.pop()
                    continue
            stack.append(a)
        return stack
