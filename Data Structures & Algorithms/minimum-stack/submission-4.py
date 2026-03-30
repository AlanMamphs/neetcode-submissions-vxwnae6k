class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val - self.min)
            if self.min > val:
                self.min = val
        else:
            self.stack.append(0)
            self.min = val
        
    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val < 0:
                self.min = self.min - val

    def top(self) -> int:
        if self.stack:
            val = self.stack[-1]
            if val > 0:
                return val + self.min
            return self.min      

    def getMin(self) -> int:
        if self.stack:
            return self.min
        
