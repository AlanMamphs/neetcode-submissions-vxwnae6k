class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        for i in range(len(res) - 2, -1, -1):
            j = i + 1
            # while there are colder days ahead of us stored at j:
            while j < len(res) and temperatures[j] <= temperatures[i]:
                if res[j] == 0: # no warmer days than j
                    j = len(res) # set out of bound
                    break
                # jump by that number of days from j, mb that day is warmer than i
                j += res[j]

            if j < len(res): # while loop found warmer day at j. out of bound if not found
                # store
                res[i] = j - i
        
        return res
                