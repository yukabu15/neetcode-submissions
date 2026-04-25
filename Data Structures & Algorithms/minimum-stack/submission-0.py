class MinStack:

    def __init__(self):
        self.q = deque()
        self.min_stack = []

    def push(self, val: int) -> None:
        self.q.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.q.pop()
        self.min_stack.pop()        

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
