class MinStack:

    def __init__(self):
        self.stack = []
        self.queue = deque()
        self.setlist = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.setlist[val] += 1
        if self.queue and val <= self.queue[-1]:
            self.queue.append(val)
        else:
            self.queue.appendleft(val)

    def pop(self) -> None:
        temp = self.stack.pop()
        self.setlist[temp] -= 1

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        while self.queue and self.setlist[self.queue[-1]] == 0:
            self.queue.pop()
        return self.queue[-1] if self.queue else 0

        
