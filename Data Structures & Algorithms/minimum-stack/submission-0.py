class MinStack:

    def __init__(self):
        self.stack = []
        self.min_vals = []

    def push(self, val: int) -> None:
        if len(self.min_vals) == 0:
            self.min_vals.append(val)
        else:
            curr_min = self.min_vals[-1]
            if val < curr_min:
                self.min_vals.append(val)
            else:
                self.min_vals.append(curr_min)

        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            raise ValueError("Stack is empty")
        
        self.stack.pop()
        self.min_vals.pop()
        
    def top(self) -> int:
        if len(self.stack) == 0:
            raise ValueError("Stack is empty")
        
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            raise ValueError("Stack is empty")
        
        return self.min_vals[-1]
