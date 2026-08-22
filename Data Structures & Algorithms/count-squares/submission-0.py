class CountSquares:

    def __init__(self):
        self.counts = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.counts[x][y] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        # if not :
        #     return 0
        print(self.counts[x1][y1])
        res = 0
        for y2 in self.counts[x1].keys():
            if y2 == y1:
                continue
            diff = abs(y1 - y2)
            left = x1 - diff
            right = x1 + diff
        

            res += 1 * self.counts[x1][y2] * self.counts[right][y1] * self.counts[right][y2]
            res += 1 * self.counts[x1][y2] * self.counts[left][y1] * self.counts[left][y2]
        
        return res

        
