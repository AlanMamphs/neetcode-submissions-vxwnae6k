class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l = -1
        r = len(people)
        curr_p = 0
        curr_w = 0
        # print(list(enumerate(people)))
        while l + 1 < r or curr_w:
            if l < r and curr_w < limit and curr_p < 2:
                if curr_w + people[r - 1] <= limit:
                    r -= 1
                    curr_w += people[r]
                    curr_p += 1
                    # print("Choose", r,  people[r])
                    continue
                elif curr_w + people[l + 1] <= limit:
                    l += 1
                    curr_w += people[l]
                    curr_p += 1
                    # print("Choose", l, people[l])
                    continue
            curr_w = 0
            curr_p = 0
            boats += 1
        return boats