from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            # The heaviest person always needs a boat.
            if people[left] + people[right] <= limit:
                left += 1  # Pair with the lightest person.

            right -= 1
            boats += 1

        return boats