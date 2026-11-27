class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_by_position = sorted(zip(position, speed), reverse=True)
        last_slowest = 0
        count = 0
        for p, s in speed_by_position:
            time = (target - p) / s

            if time > last_slowest:
                count += 1
                last_slowest = time
        return count
