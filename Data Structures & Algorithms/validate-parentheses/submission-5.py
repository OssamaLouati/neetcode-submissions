class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            ")": "(",
            "]":"[",
            "}":"{"
            }
        
        for c in s:
            if len(stack) > 0:
                if m.get(c) == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        return len(stack) == 0