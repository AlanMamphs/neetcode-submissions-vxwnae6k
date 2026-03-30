class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = 0

        prev = 0

        for p, s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            if prev < time:
                fleets += 1
                prev = time
        return fleets           