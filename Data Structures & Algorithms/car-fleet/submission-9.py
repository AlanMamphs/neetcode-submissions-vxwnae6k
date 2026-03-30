class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = 1

        prev = 0

        for p, s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            if prev < time:
                if prev != 0:
                    fleets += 1
                prev = time
        return fleets           