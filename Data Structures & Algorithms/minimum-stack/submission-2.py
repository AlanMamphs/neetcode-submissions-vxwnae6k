class MinStack:

    def __init__(self):
        self.value = []

    def push(self, val: int) -> None:
        self.value.append((val, min(self.value[-1][1] if self.value else val, val)))

    def pop(self) -> None:
        if len(self.value):
            val = self.value.pop()
            return val[0]
    def top(self) -> int:
        if len(self.value):
            return self.value[-1][0]

    def getMin(self) -> int:
        if len(self.value):
            return self.value[-1][1]
